from typing import List

from app.model.news import News
from app.schema.common.news import ModelNews
from app.schema.input.news import PostNewsIn
from app.schema.output.news import GetNewsOut, PostNewsOut


def get_news() -> List[GetNewsOut]:
    db = News()
    resp = db.get()
    return [GetNewsOut.from_orm(r) for r in resp]


def post_news(data: PostNewsIn) -> PostNewsOut:
    db = News()
    new_data = ModelNews.from_orm(data)
    resp = db.add(data=new_data)
    return PostNewsOut.from_orm(resp)
