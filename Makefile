.PHONY: check_all linter_check format_code test coverage_test type_check run_app_on_docker build_run_app_on_docker run_app

check_all: linter_check test

linter_check:
	poetry run black --check -l 80 .

format_code:
	poetry run black -l 80 .

test:
	poetry run pytest

coverage_test:
	poetry run coverage run -m pytest -v && poetry run coverage report -m

type_check:
	poetry run mypy src

run_app_on_docker:
	docker-compose up

build_run_app_on_docker:
	docker-compose up --build

run_app:
	poetry run python -m src
