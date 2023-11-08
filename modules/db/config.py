from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    pg_dsn: PostgresDsn = 'postgresql+asyncpg://fastapi:fastapi@127.0.0.1:5433/fastapi'


settings = Settings()
