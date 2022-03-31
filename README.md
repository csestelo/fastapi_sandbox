## Project's Setup:
1. Install Poetry: https://python-poetry.org/docs/#installation
2. Run: `poetry install`

## Commands:

- Linter check: `poetry run black --check -l 80 .`
- Linter formatting: `poetry run black -l 80 .`
- Tests: `poetry run pytest`
- Tests with coverage: `poetry run coverage run -m pytest && poetry run coverage report -m`
- Type checking: `poetry run mypy fast_api_sandbox`
