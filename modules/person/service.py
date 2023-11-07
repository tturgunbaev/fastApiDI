import uuid

from .repositories.db_repo import PersonRepo
from .schemas.base_schemas import Person

repo = PersonRepo()


class PersonService:

    @staticmethod
    async def get(id_: uuid.UUID) -> Person | None:
        return await repo.get(id_)

    @staticmethod
    async def create(person: Person) -> uuid.UUID:
        return await repo.create(person)

    @staticmethod
    async def get_all() -> list:
        return await repo.get_all()

    @staticmethod
    async def delete(id_: uuid.UUID):
        return await repo.delete(id_)
