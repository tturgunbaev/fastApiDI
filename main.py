from fastapi import FastAPI

from modules.person.api import router

app = FastAPI()

app.include_router(router)


@app.get('/')
async def hello() -> dict:
    return {'message': 'Hello world'}
