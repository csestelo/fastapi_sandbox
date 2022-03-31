## Project's Setup:
1. Install Poetry: https://python-poetry.org/docs/#installation
2. Run: `poetry install`
3. Run App locally: `python -m fast_api_sandbox`
4. Swagger with endpoints' doc will be available at http://<APP_HOST>:<APP_PORT>>/docs. Defaults to: `http://127.0.0.1:5000/docs`


## Commands:
- Linter check: `poetry run black --check -l 80 .`
- Linter formatting: `poetry run black -l 80 .`
- Tests: `poetry run pytest`
- Tests with coverage: `poetry run coverage run -m pytest -v && poetry run coverage report -m`
- Type checking: `poetry run mypy fast_api_sandbox`
