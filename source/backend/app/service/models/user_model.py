from pydantic import BaseModel


class UserReadModel(BaseModel):
    id: int
    name: str
    email: str
