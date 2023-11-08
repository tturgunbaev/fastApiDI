import uuid

from pydantic import TypeAdapter
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete

from ..schemas.base_schemas import Person
from ..db.base_methods import BaseDBRepo
from ..db.models import PersonDB


class PersonDBRepo(BaseDBRepo):

    def __init__(self, db_session: AsyncSession):
        self._session = db_session

    async def get(self, id_: uuid.UUID) -> Person | None:
        result = await self._session.get(PersonDB, id_)
        return Person.model_validate(result) if result else result

    async def create(self, person: Person) -> uuid.UUID:
        db_model = PersonDB(**person.model_dump(exclude_none=True))
        self._session.add(db_model)
        await self._session.commit()
        return person.id_

    async def get_all(self) -> list[Person]:
        result = await self._session.scalars(select(PersonDB))
        person_list_validator = TypeAdapter(list[Person])
        return person_list_validator.validate_python(result)

    async def delete(self, id_: uuid.UUID):
        await self._session.execute(
            delete(PersonDB).where(PersonDB.id_ == id_)
        )
