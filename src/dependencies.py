from fastapi import FastAPI, Request

from src.models import Base
from src.services.repository import DBRepo
from src.services.db import db_connection


def setup_app_deps(app: FastAPI):
    engine, session = db_connection()
    app.state.db_engine = engine
    app.state.db_repo = DBRepo(db_session=session)


async def create_db_schema(app: FastAPI):
    async with app.state.db_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def shutdown_app_deps(app: FastAPI):
    await app.state.db_engine.dispose()


def get_db_repo(request: Request):
    return request.app.state.db_repo
