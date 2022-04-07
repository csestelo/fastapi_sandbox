import pytest

from httpx import AsyncClient
from sqlalchemy import text
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.orm import sessionmaker

from config import settings
from src.app import app
from src.services.db import db_connection
from src.models import Base


@pytest.fixture
def anyio_backend():
    """To avoid running tests twice.
    https://anyio.readthedocs.io/en/stable/testing.html#specifying-the-backends-to-run-on
    """
    return "asyncio"


@pytest.fixture
async def mocked_client(scope="session") -> AsyncClient:
    async with AsyncClient(
        app=app, base_url=f"http://{settings.APP_HOST}"
    ) as ac:
        yield ac


@pytest.fixture
async def create_test_database(scope="session"):
    test_db_name = "test"
    engine, _ = db_connection()
    try:
        async with engine.connect() as conn:
            await conn.execute(text("commit"))
            await conn.execute(text(f"CREATE DATABASE {test_db_name}"))
    except ProgrammingError:
        # To avoid class 'asyncpg.exceptions.DuplicateDatabaseError
        pass

    await engine.dispose()
    settings.DB_DATABASE = test_db_name


@pytest.fixture
async def db_session(create_test_database, scope="session") -> sessionmaker:
    engine, session = db_connection()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield session

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
