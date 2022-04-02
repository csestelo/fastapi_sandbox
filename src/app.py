from fastapi import FastAPI

from src.routes import customer
from src.routes import health_check

app = FastAPI()

app.include_router(customer.router)
app.include_router(health_check.router)
