from sqlalchemy.ext.asyncio import (
    create_async_engine, async_sessionmaker, AsyncSession
)

from src.config import settings

engine = create_async_engine(str(settings.pg_dsn))


async def get_session_maker():
    return async_sessionmaker(
            bind=engine,
            class_=AsyncSession
        )
