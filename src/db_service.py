from typing import Tuple

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    AsyncEngine,
)
from sqlalchemy.orm import sessionmaker, declarative_base  # type:ignore

from config import settings


async def db_connection() -> Tuple[AsyncEngine, sessionmaker]:
    # `echo` parameter logs all SQLs emitted
    engine = create_async_engine(settings.DATABASE_URI, echo=settings.DB_ECHO)
    async_session = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )

    return engine, async_session
