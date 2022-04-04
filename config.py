from pydantic import BaseSettings
from sqlalchemy.engine import URL  # type: ignore


class Config(BaseSettings):
    APP_PORT: int = 5000
    APP_HOST: str = "0.0.0.0"
    DB_HOST: str = "localhost"
    DB_USERNAME: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_DATABASE: str = "register"

    @property
    def DATABASE_URI(self):
        return URL.create(
            drivername="postgresql+asyncpg",
            username=self.DB_USERNAME,
            password=self.DB_PASSWORD,
            host=self.DB_HOST,
            database=self.DB_DATABASE,
        )


settings = Config()
