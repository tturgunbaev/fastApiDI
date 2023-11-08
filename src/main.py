from fastapi import FastAPI
from .modules import api

app = FastAPI()

app.include_router(api.router)


@app.get('/')
async def hello() -> dict:
    return {'message': 'Hello world'}
