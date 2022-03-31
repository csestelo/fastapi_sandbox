import uvicorn  # type: ignore

from config import settings

if __name__ == "__main__":
    uvicorn.run(
        "fast_api_sandbox.app:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
    )
