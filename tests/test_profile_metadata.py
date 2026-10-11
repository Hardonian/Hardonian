import datetime as dt
import importlib.util
import unittest
from copy import deepcopy
from pathlib import Path
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location(
    "profile_metadata", Path(__file__).parents[1] / "scripts/profile-metadata.py"
)
metadata = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(metadata)


def valid_manifest():
    project = {
        "name": "Example",
        "role": "Observe",
        "maturity": "beta",
        "language": "Go",
        "problem": "A concrete problem.",
        "proof": "A public proof.",
        "repository": "https://github.com/Hardonian/Example",
        "documentation": "https://github.com/Hardonian/Example/blob/main/docs/ARCHITECTURE.md",
        "evidence": "https://github.com/Hardonian/Example/blob/main/spec/README.md",
        "ci_workflow": "ci.yml",
    }
    projects = []
    for index in range(4):
        item = deepcopy(project)
        item["name"] = f"Example{index}"
        item["repository"] = f"https://github.com/Hardonian/Example{index}"
        projects.append(item)
    return {"verified_on": "2026-09-19", "max_age_days": 90, "projects": projects}


class ProfileMetadataTests(unittest.TestCase):
    def test_renders_four_projects_and_live_ci(self):
        manifest = valid_manifest()
        metadata.validate_manifest(manifest, today=dt.date(2026, 9, 19))
        output = metadata.render(manifest)
        self.assertEqual(output.count("badge.svg"), 4)
        self.assertIn("Public project metadata last verified **2026-09-19**", output)

    def test_rejects_stale_metadata(self):
        manifest = valid_manifest()
        with self.assertRaisesRegex(metadata.MetadataError, "stale"):
            metadata.validate_manifest(manifest, today=dt.date(2027, 1, 1))

    def test_rejects_invalid_maturity(self):
        manifest = valid_manifest()
        manifest["projects"][0]["maturity"] = "production-ish"
        with self.assertRaisesRegex(metadata.MetadataError, "invalid maturity"):
            metadata.validate_manifest(manifest, today=dt.date(2026, 9, 19))

    def test_replaces_only_generated_section(self):
        source = "before\n<!-- profile-projects:start -->\nold\n<!-- profile-projects:end -->\nafter\n"
        generated = "<!-- profile-projects:start -->\nnew\n<!-- profile-projects:end -->\n"
        result = metadata.replace_generated_section(source, generated)
        self.assertEqual(result, "before\n<!-- profile-projects:start -->\nnew\n<!-- profile-projects:end -->\nafter\n")

    def test_translates_github_artifacts_to_api_urls(self):
        self.assertEqual(
            metadata.github_api_url(
                "https://github.com/Hardonian/AgentPCAP/blob/main/docs/ARCHITECTURE.md"
            ),
            "https://api.github.com/repos/Hardonian/AgentPCAP/contents/docs/ARCHITECTURE.md?ref=main",
        )
        self.assertEqual(
            metadata.github_api_url("https://github.com/Hardonian/mcpwall/releases/tag/v1.0.5"),
            "https://api.github.com/repos/Hardonian/mcpwall/releases/tags/v1.0.5",
        )

    def test_stale_manifest_can_be_validated_for_refresh(self):
        metadata.validate_manifest(
            valid_manifest(),
            today=dt.date(2027, 1, 1),
            enforce_freshness=False,
        )

    @patch.object(metadata, "README_PATH")
    @patch.object(metadata, "MANIFEST_PATH")
    @patch.object(metadata, "verify_remote")
    def test_refresh_updates_manifest_and_readme_with_remote(self, mock_verify_remote, mock_manifest_path, mock_readme_path):
        manifest = valid_manifest()
        mock_readme_path.read_text.return_value = (
            "header\n<!-- profile-projects:start -->\nold\n<!-- profile-projects:end -->\nfooter\n"
        )

        today_mock = dt.date(2026, 10, 10)
        with patch("datetime.datetime") as mock_datetime:
            mock_datetime.now.return_value.date.return_value = today_mock
            metadata.refresh(manifest, remote=True)

        mock_verify_remote.assert_called_once_with(manifest)
        self.assertEqual(manifest["verified_on"], "2026-10-10")
        mock_manifest_path.write_text.assert_called_once()
        mock_readme_path.write_text.assert_called_once()
        written_readme = mock_readme_path.write_text.call_args[0][0]
        self.assertIn("Public project metadata last verified **2026-10-10**", written_readme)

    @patch.object(metadata, "README_PATH")
    @patch.object(metadata, "MANIFEST_PATH")
    @patch.object(metadata, "verify_remote")
    def test_refresh_skips_remote_when_remote_false(self, mock_verify_remote, mock_manifest_path, mock_readme_path):
        manifest = valid_manifest()
        manifest["verified_on"] = "2020-01-01"  # stale manifest
        mock_readme_path.read_text.return_value = (
            "header\n<!-- profile-projects:start -->\nold\n<!-- profile-projects:end -->\nfooter\n"
        )

        today_mock = dt.date(2026, 10, 10)
        with patch("datetime.datetime") as mock_datetime:
            mock_datetime.now.return_value.date.return_value = today_mock
            metadata.refresh(manifest, remote=False)

        mock_verify_remote.assert_not_called()
        self.assertEqual(manifest["verified_on"], "2026-10-10")
        mock_manifest_path.write_text.assert_called_once()
        mock_readme_path.write_text.assert_called_once()

    @patch.object(metadata, "README_PATH")
    @patch.object(metadata, "verify_remote")
    def test_check_passes_when_synced(self, mock_verify_remote, mock_readme_path):
        manifest = valid_manifest()
        rendered = metadata.render(manifest)
        synced_readme = f"header\n{rendered}\nfooter\n"
        mock_readme_path.read_text.return_value = synced_readme

        with patch("datetime.datetime") as mock_datetime:
            mock_datetime.now.return_value.date.return_value = dt.date(2026, 9, 19)
            metadata.check(manifest, remote=True)

        mock_verify_remote.assert_called_once_with(manifest)

    @patch.object(metadata, "README_PATH")
    def test_check_raises_metadata_error_when_out_of_sync(self, mock_readme_path):
        manifest = valid_manifest()
        out_of_sync_readme = "header\n<!-- profile-projects:start -->\noutdated\n<!-- profile-projects:end -->\nfooter\n"
        mock_readme_path.read_text.return_value = out_of_sync_readme

        with patch("datetime.datetime") as mock_datetime:
            mock_datetime.now.return_value.date.return_value = dt.date(2026, 9, 19)
            with self.assertRaisesRegex(metadata.MetadataError, "out of sync"):
                metadata.check(manifest, remote=False)


if __name__ == "__main__":
    unittest.main()
