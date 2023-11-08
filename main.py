from fastapi import FastAPI

from modules import person

app = FastAPI()
app.person_container = person.containers.Container()

app.include_router(person.api.router)


@app.get('/')
async def hello() -> dict:
    return {'message': 'Hello world'}
