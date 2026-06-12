Repository snapshot

- Minimal Python repository. Current working tree contains a single top-level script: fun_01.py (0 bytes). No package layout, no tests, no CI, no linters detected.

Build, test and lint commands

- None configured in this repository right now.
- If pytest is added later, run a single test with:
  - python -m pytest tests/test_file.py::test_name
  - or to run tests matching -k: python -m pytest -k "test_substring"
- If unittest is used, run a single test with:
  - python -m unittest tests.test_module.TestClass.test_method
- Linting (if you add flake8/ruff/black): run them directly, e.g. ruff check <path> or python -m black --check <path>.

High-level architecture (big picture)

- Current state: single-script repository. No packages, modules, or entry points.
- Expected scaling pattern for this repo:
  - Use src/ or a top-level package for library code (e.g., src/fun_in_py/)
  - Keep CLI or runnable scripts in bin/ or at top-level scripts
  - Tests in tests/ (pytest recommended)
  - Configuration files at repo root: pyproject.toml or setup.cfg, requirements.txt or poetry/poetry.lock

Key conventions and repo-specific notes

- Filenames use snake_case (example: fun_01.py). Follow that convention when adding modules.
- No framework conventions (web, CI, or packaging) are present — new contributors should add a clear single source of truth (pyproject.toml or setup.cfg) if they introduce tooling.
- Keep scripts small and single-purpose; convert to a package if functionality grows.

AI assistant and tool config files checked

- Searched for common assistant config files and none were found: README.md, CONTRIBUTING.md, CLAUDE.md, .cursorrules, AGENTS.md, .windsurfrules, CONVENTIONS.md, AIDER_CONVENTIONS.md, .clinerules, or .copilot-instructions.md (prior) were not present.

How to help future Copilot sessions

- If adding tests, add a pyproject.toml or setup.cfg and a tox.ini or GitHub Actions workflow so Copilot can infer test/lint commands.
- Add a short README with the project intent and expected layout; Copilot sessions rely on that to provide targeted suggestions.
- When introducing tooling, include top-level scripts or GitHub Actions names (e.g., "pytest", "lint", "build") so Copilot can detect common commands automatically.

Contact / follow-ups

- This file was created automatically to describe the repository state at the time of inspection. If you'd like, Copilot can:
  - Add a recommended project scaffold (pyproject.toml, basic pytest layout)
  - Add a GitHub Actions workflow for tests and linting
  - Create a README or CONTRIBUTING template to document conventions

Summary

- Created .github/copilot-instructions.md describing the current minimal repo state, commands to use if common tools are later added, high-level architecture guidance, and detected absent assistant configs.

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>