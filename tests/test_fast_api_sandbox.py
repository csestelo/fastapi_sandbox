from http import HTTPStatus


def test_home_ping(mocked_client):
    resp = mocked_client.get("/")
    assert resp.status_code == HTTPStatus.OK
    assert resp.json() == {"message": "PONG! App running!"}


def test_health_check(mocked_client):
    # implement real health checks for app
    resp = mocked_client.get("/")
    assert resp.status_code == HTTPStatus.OK
    assert resp.json() == {"message": "PONG! App running!"}
