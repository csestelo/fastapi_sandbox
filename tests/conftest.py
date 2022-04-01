import pytest

from httpx import AsyncClient

from config import settings
from src.app import app


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
