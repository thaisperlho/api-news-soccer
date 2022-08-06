from pydantic import BaseModel


class PostNewsIn(BaseModel):
    title: str
    description: str
    image: str
    link: str

    class Config:
        orm_mode = True
