import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

from app.core.constants.base import Environment

load_dotenv()


class Settings(BaseSettings):
    app_title: str = "Cadastral service"
    app_description: str = "Service for creating cadastral numbers"
    secret: str = "where is my money lebowski"
    environment: Environment = Environment.LOCAL
    redis_password: str
    redis_host: str
    redis_port: str
    celery_redis_db: str

    @property
    def celery_broker_url(self):
        return f"redis://:{self.redis_password}@{os.getenv('REDIS_HOST')}:{self.redis_port}/{self.celery_redis_db}"

    @property
    def celery_result_backend(self):
        return f"redis://:{self.redis_password}@{os.getenv('REDIS_HOST')}:{self.redis_port}/{self.celery_redis_db}"

    @property
    def is_prod(self):
        return self.environment == Environment.PROD


settings = Settings()
settings.redis_host = "localhost" if settings.environment == Environment.LOCAL else settings.redis_host
