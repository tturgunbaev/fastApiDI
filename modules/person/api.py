import uuid

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, HTTPException, Depends

from .schemas.base_schemas import Person, PersonIn
from .engines.engine import PersonEngine
from . import Container

router = APIRouter(prefix='/persons', tags=['persons'])


@router.get('/')
@inject
async def get_persons(
        engine: PersonEngine = Depends(Provide[Container.engine])
) -> list[Person]:
    return await engine.get_all()


@router.post('/')
@inject
async def create_person(
        person: PersonIn,
        engine: PersonEngine = Depends(Provide[Container.engine])
) -> uuid.UUID:
    person = Person(**person.model_dump())
    return await engine.create(person)


@router.get('/{id_}/')
@inject
async def get_person(
        id_: uuid.UUID,
        engine: PersonEngine = Depends(Provide[Container.engine])
) -> Person:
    result = await engine.get(id_)
    if not result:
        raise HTTPException(status_code=404, detail='Not Found')
    return result


@router.delete('/{id_}/', status_code=204)
@inject
async def delete_person(
        id_: uuid.UUID,
        engine: PersonEngine = Depends(Provide[Container.engine])
) -> None:
    await engine.delete(id_)
