from http import HTTPStatus

import pytest


@pytest.mark.anyio
async def test_home_ping(mocked_client):
    resp = await mocked_client.get("/")
    assert resp.status_code == HTTPStatus.OK
    assert resp.json() == {"message": "PONG! App running!"}


@pytest.mark.anyio
async def test_health_check(mocked_client):
    # implement real health checks for app
    resp = await mocked_client.get("/")
    assert resp.status_code == HTTPStatus.OK
    assert resp.json() == {"message": "PONG! App running!"}
