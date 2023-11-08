from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.ext.asyncio import (
    create_async_engine, async_sessionmaker, AsyncSession
)

from modules.db.config import settings

engine = create_async_engine(str(settings.pg_dsn))

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession
)


async def async_session() -> Callable[..., AbstractContextManager[AsyncSession]]:
    async with AsyncSessionLocal() as session:
        yield session
