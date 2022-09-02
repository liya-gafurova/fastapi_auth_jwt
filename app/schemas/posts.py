from typing import Optional
from uuid import UUID

from pydantic import BaseModel
from pydantic.schema import datetime


class PostDB(BaseModel):
    id: UUID
    title: str
    text: str
    created: datetime


class PostCreate(BaseModel):
    title: str
    text: str


class PostRead(BaseModel):
    id: str
    title: str
    text: str
    created: str


class PostUpdate(BaseModel):
    title: Optional[str]
    text: Optional[str]
