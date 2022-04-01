from fastapi import APIRouter


router = APIRouter()


@router.get("/")
@router.get("/health_check")
async def ping():
    return {"message": "PONG! App running!"}
