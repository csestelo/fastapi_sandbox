from pydantic import BaseSettings


class Config(BaseSettings):
    APP_PORT: int = 5000
    APP_HOST: str = "0.0.0.0"


settings = Config()
