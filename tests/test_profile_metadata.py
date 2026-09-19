import datetime as dt
import importlib.util
import unittest
from copy import deepcopy
from pathlib import Path

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


if __name__ == "__main__":
    unittest.main()
