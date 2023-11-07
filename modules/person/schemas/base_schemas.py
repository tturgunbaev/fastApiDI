import uuid

from pydantic import BaseModel, Field


class Person(BaseModel):
    id_: uuid.UUID = Field(default_factory=uuid.uuid4)
    name: str | None
    age: int | None


class PersonIn(BaseModel):
    name: str
    age: int
