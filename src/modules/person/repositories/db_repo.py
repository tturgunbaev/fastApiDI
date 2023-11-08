import uuid

from pydantic import TypeAdapter
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy import select, delete

from ..schemas.base_schemas import Person
from ..db.models import PersonDB
from .db_abc import BaseDBRepo


class PersonDBRepo(BaseDBRepo):

    def __init__(self, session: async_sessionmaker[AsyncSession]):
        self._session = session

    async def get(self, id_: uuid.UUID) -> Person | None:
        async with self._session() as s:
            result = await s.get(PersonDB, id_)
        return Person.model_validate(result) if result else result

    async def create(self, person: Person) -> uuid.UUID:
        db_model = PersonDB(**person.model_dump(exclude_none=True))
        async with self._session() as s:
            s.add(db_model)
            await s.commit()
        return person.id_

    async def get_all(self) -> list[Person]:
        async with self._session() as s:
            result = await s.scalars(select(PersonDB))
        person_list_validator = TypeAdapter(list[Person])
        return person_list_validator.validate_python(result)

    async def delete(self, id_: uuid.UUID):
        async with self._session() as s:
            await s.execute(
                delete(PersonDB).where(PersonDB.id_ == id_)
            )
