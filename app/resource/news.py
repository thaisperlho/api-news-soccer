from typing import List

from app.controller import news
from app.schema.input.news import PostNewsIn
from app.schema.output.news import GetNewsOut, PostNewsOut
from fastapi import APIRouter, FastAPI


def init_app(app: FastAPI):
    router = APIRouter(prefix="/v1")

    @router.get("/news", response_model=List[GetNewsOut])
    def get_news():
        return news.get_news()

    @router.post("/news", response_model=PostNewsOut)
    def post_news(data: PostNewsIn):
        return news.post_news(data=data)

    @router.put("/news")
    def put_news():
        return ""

    @router.delete("/news")
    def delete_news():
        return ""

    app.include_router(router=router)
