.PHONY: check_all linter_check format_code test_on_docker coverage_test type_check build_run_app_on_docker run_app_on_docker start_app_deps

check_all: linter_check test_on_docker type_check

linter_check:
	poetry run black --check -l 80 .

format_code:
	poetry run black -l 80 .

test_on_docker: start_app_deps
	poetry run pytest

coverage_test: start_app_deps
	poetry run coverage run -m pytest -v && poetry run coverage report -m

type_check:
	poetry run mypy src

build_run_app_on_docker:
	docker-compose up --build

run_app_on_docker:
	docker-compose up

start_app_deps:
	docker-compose up -d db
