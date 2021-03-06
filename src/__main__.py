import uvicorn  # type: ignore

from config import settings

if __name__ == "__main__":
    uvicorn.run(
        "src.app:app",
        reload=True,
        host=settings.APP_HOST,
        port=settings.APP_PORT,
    )
