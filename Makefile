linter_check:
	poetry run black --check -l 80 .

linter_format:
	poetry run black -l 80 .

test:
	poetry run pytest

coverage_test:
	poetry run coverage run -m pytest -v && poetry run coverage report -m

type_checking:
	poetry run mypy src
