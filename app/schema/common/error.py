from pydantic import BaseModel


class ModelError(BaseModel):
    detail: str
