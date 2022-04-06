from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from config import logger


class DBRepo:
    def __init__(self, db_session: sessionmaker):
        self.session = db_session

    async def is_db_conn_ok(self) -> bool:
        try:
            async with self.session() as ss:
                result = await ss.execute(text("SELECT 1"))
                return result.scalars().first() == 1

        except Exception as e:
            logger.error(
                {"msg": "No connection with database.", "exception": str(e)}
            )
            return False
