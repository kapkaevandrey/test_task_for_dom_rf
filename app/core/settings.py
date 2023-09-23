from pydantic import BaseSettings

from app.core.constants.base import Environment


class Settings(BaseSettings):
    app_title: str = "Cadastral service"
    app_description: str = "Service for creating cadastral numbers"
    secret: str = "where is my money lebowski"
    environment: Environment = Environment.LOCAL

    class Config:
        env_file = ".env"

    @property
    def is_prod(self):
        return self.environment == Environment.PROD


settings = Settings()
