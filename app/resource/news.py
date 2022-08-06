from typing import List

from app.controller import news
from app.schema.common.error import ModelError
from app.schema.input.news import PostNewsIn, PutNewsIn
from app.schema.output.news import DelNewsOut, GetNewsOut, PostNewsOut, PutNewsOut
from fastapi import APIRouter, FastAPI


def init_app(app: FastAPI):
    responses = {400: {"description": "invalid id", "model": ModelError}}
    router = APIRouter(prefix="/v1", tags=["News"])

    @router.get("/news", response_model=List[GetNewsOut])
    def get_news():
        return news.get_news()

    @router.get("/news/{id}", response_model=GetNewsOut)
    def get_news_by_id(id: int):
        return news.get_news_by_id(id=id)

    @router.post("/news", response_model=PostNewsOut)
    def post_news(data: PostNewsIn):
        return news.post_news(data=data)

    @router.put("/news/{id}", response_model=PutNewsOut, responses=responses)
    def put_news(data: PutNewsIn, id: int):
        return news.put_news(data=data, id=id)

    @router.delete("/news/{id}", response_model=DelNewsOut, responses=responses)
    def delete_news(id: int):
        return news.del_news(id=id)

    app.include_router(router=router)
