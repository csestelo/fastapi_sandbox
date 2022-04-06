from http import HTTPStatus

from fastapi import APIRouter, Depends, Response

from src.dependencies import get_db_repo
from src.services.repository import DBRepo

router = APIRouter()


@router.get("/")
@router.get("/health_check")
async def ping(response: Response, db_repo: DBRepo = Depends(get_db_repo)):
    app_status = "UP"
    has_conn = await db_repo.is_db_conn_ok()

    if not has_conn:
        response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        app_status = "DOWN"

    return {
        "message": f"App {app_status}!",
        "dependencies": {"database": has_conn},
    }
