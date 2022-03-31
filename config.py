from pydantic import BaseSettings


class Config(BaseSettings):
    APP_PORT: int = 5000
    APP_HOST: str = "127.0.0.1"


settings = Config()
