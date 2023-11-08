import uuid

from ..repositories.db_repo import PersonDBRepo
from ..schemas.base_schemas import Person


class PersonEngine:

    def __init__(self, repo: PersonDBRepo):
        self._repo = repo

    async def get(self, id_: uuid.UUID) -> Person | None:
        return await self._repo.get(id_)

    async def create(self, person: Person) -> uuid.UUID:
        return await self._repo.create(person)

    async def get_all(self) -> list[Person]:
        return await self._repo.get_all()

    async def delete(self, id_: uuid.UUID):
        return await self._repo.delete(id_)
