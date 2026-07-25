import os
print("Running pre-commit tests.")
os.system("pnpm dlx markdownlint-cli -c .markdownlint-cli2.jsonc '**/*.md'")
