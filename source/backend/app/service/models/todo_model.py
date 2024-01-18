from datetime import datetime
from pydantic import BaseModel


class TodoCreateModel(BaseModel):
    user_id: int
    title: str


class TodoUpdateModel(BaseModel):
    id: int
    title: str


class TodoReadModel(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime
    user_id: int
    title: str
    is_done: bool
