from http import HTTPStatus
from unittest.mock import MagicMock, AsyncMock

import pytest

from src.app import app
from src.dependencies import get_db_repo


@pytest.mark.anyio
async def test_health_check_ok(mocked_client):
    expected_resp = {"dependencies": {"database": True}, "message": "App UP!"}

    def _mocked_db_repo():
        return MagicMock(is_db_conn_ok=AsyncMock(return_value=True))

    app.dependency_overrides[get_db_repo] = _mocked_db_repo

    for endpoint in ["/", "health_check"]:
        resp = await mocked_client.get(endpoint)

        assert resp.status_code == HTTPStatus.OK
        assert expected_resp == resp.json()


@pytest.mark.anyio
async def test_health_check_fails(mocked_client):
    expected_resp = {
        "dependencies": {"database": False},
        "message": "App DOWN!",
    }

    def _mocked_db_repo():
        return MagicMock(is_db_conn_ok=AsyncMock(return_value=False))

    app.dependency_overrides[get_db_repo] = _mocked_db_repo

    for endpoint in ["/", "health_check"]:
        resp = await mocked_client.get(endpoint)

        assert resp.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
        assert expected_resp == resp.json()
