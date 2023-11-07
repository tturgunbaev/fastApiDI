import uuid

from fastapi import APIRouter, HTTPException

from modules.person.schemas.base_schemas import Person, PersonIn
from modules.person.service import PersonService

router = APIRouter(prefix='/persons', tags=['persons'])


@router.get('/')
async def get_persons() -> list[Person]:
    return await PersonService.get_all()


@router.post('/')
async def create_person(person: PersonIn) -> uuid.UUID:
    person = Person(**person.model_dump())
    return await PersonService.create(person)


@router.get('/{id_}/')
async def get_person(id_: uuid.UUID) -> Person:
    result = await PersonService.get(id_)
    if not result:
        raise HTTPException(status_code=404, detail='Not Found')
    return result


@router.delete('/{id_}/')
async def delete_person(id_: uuid.UUID) -> None:
    await PersonService.delete(id_)
