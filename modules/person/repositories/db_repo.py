import uuid
from typing import List

from modules.person.schemas.base_schemas import Person
from .db_interfaces import BaseDBRepo
from .db import db


class PersonRepo(BaseDBRepo):

    async def get(self, id_: uuid.UUID) -> Person | None:
        result = db.get(id_)
        return Person(**result) if result else result

    async def create(self, person: Person) -> uuid.UUID:
        db[person.id_] = person.model_dump()
        return person.id_

    async def get_all(self) -> List[dict]:
        return db.values()

    async def delete(self, id_: uuid.UUID):
        if id_ in db:
            del db[id_]
