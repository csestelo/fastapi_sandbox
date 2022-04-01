## Project's Setup:
1. Install Poetry: https://python-poetry.org/docs/#installation
2. Run: `poetry install`
3. Run App locally with: 
   1. `make run_app_on_docker`: docker-compose to make available app + dependencies. 
   2. `make run_app`: run (only) the app, no docker needed.
4. Swagger with documentation of all endpoints will be available at http://<APP_HOST>:<APP_PORT>>/docs. Defaults to: `http://127.0.0.1:5000/docs`


## Commands:
For running `type checking`, `linter`, and `tests` check Makefile commands.
