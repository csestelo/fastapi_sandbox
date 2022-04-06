from fastapi import FastAPI

from src.dependencies import create_db_schema, setup_app_deps, shutdown_app_deps
from src.controlers import customer
from src.controlers import health_check

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    setup_app_deps(app)
    # here to make developing easier
    await create_db_schema(app)


@app.on_event("shutdown")
async def shutdown_event():
    await shutdown_app_deps(app)


app.include_router(customer.router)
app.include_router(health_check.router)
