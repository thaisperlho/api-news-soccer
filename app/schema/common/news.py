from datetime import datetime

from pydantic import BaseModel


class ModelNews(BaseModel):
    id: int = None
    title: str
    description: str
    image: str
    link: str
    created_at: datetime = None
    updated_at: datetime = None

    class Config:
        orm_mode = True
