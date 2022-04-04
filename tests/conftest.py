from typing import AsyncIterable

import pytest

from httpx import AsyncClient
from sqlalchemy.orm import sessionmaker

from config import settings
from src.app import app
from src.db_service import db_connection
from src.models import Base


@pytest.fixture
def anyio_backend():
    """To avoid running tests twice.
    https://anyio.readthedocs.io/en/stable/testing.html#specifying-the-backends-to-run-on
    """
    return "asyncio"


@pytest.fixture
async def mocked_client(scope="session"):
    async with AsyncClient(
        app=app, base_url=f"http://{settings.APP_HOST}"
    ) as ac:
        yield ac


@pytest.fixture
async def db_session(scope="session") -> sessionmaker:
    engine, session = await db_connection()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield session

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
