import uuid
from datetime import datetime

from pydantic import UUID4, BaseModel, Extra, Field

from .utils import utcnow


class BookCreatePayload(BaseModel):
    title: str
    author: str

    class Config:
        extra = Extra.forbid


class BookCreated(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    title: str
    author: str
    created_at: datetime = Field(default_factory=utcnow)
