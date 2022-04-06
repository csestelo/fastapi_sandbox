from unittest.mock import MagicMock

import pytest

from src.services.repository import DBRepo


@pytest.mark.anyio
async def test_check_db_conn_success(db_session):
    repo = DBRepo(db_session=db_session)

    assert await repo.is_db_conn_ok()


@pytest.mark.anyio
async def test_check_db_conn_fail():
    repo = DBRepo(db_session=MagicMock(side_effect=Exception))

    assert not await repo.is_db_conn_ok()
