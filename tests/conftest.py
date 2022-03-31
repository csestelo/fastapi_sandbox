import pytest

from fastapi.testclient import TestClient

from fast_api_sandbox.app import app


@pytest.fixture
def mocked_client(scope="session"):
    return TestClient(app)
