import uuid

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from ...db import Base


class PersonDB(Base):
    __tablename__ = 'persons'
    id_: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    age: Mapped[int]
