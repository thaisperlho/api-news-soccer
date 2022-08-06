from datetime import datetime

from pydantic import BaseModel


class GetNewsOut(BaseModel):
    id: int
    title: str
    description: str
    image: str
    link: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class PostNewsOut(GetNewsOut):
    ...
