import uuid

from pydantic import BaseModel, Field, ConfigDict


class Person(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id_: uuid.UUID = Field(default_factory=uuid.uuid4)
    name: str | None
    age: int | None


class PersonIn(BaseModel):
    name: str
    age: int
