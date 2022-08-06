from typing import List

from app.model.news import News
from app.schema.common.news import ModelNews
from app.schema.input.news import PostNewsIn, PutNewsIn
from app.schema.output.news import DelNewsOut, GetNewsOut, PostNewsOut, PutNewsOut
from fastapi import HTTPException


def get_news() -> List[GetNewsOut]:
    db = News()
    rows = db.get()
    return [GetNewsOut.from_orm(row) for row in rows]


def get_news_by_id(id: int) -> GetNewsOut:
    db = News()
    row = db.get_by_id(id=id)
    return GetNewsOut.from_orm(row) if row else None


def post_news(data: PostNewsIn) -> PostNewsOut:
    db = News()
    new_data = ModelNews.from_orm(data)
    resp = db.add(data=new_data)
    return PostNewsOut.from_orm(resp)


def put_news(data: PutNewsIn, id: int) -> PutNewsOut:
    db = News()
    if db.get_by_id(id=id) is None:
        raise HTTPException(status_code=400, detail="id does not exists")
    new_data = ModelNews.from_orm(data)
    resp = db.change(data=new_data, id=id)
    return PutNewsOut.from_orm(resp)


def del_news(id: int) -> DelNewsOut:
    db = News()
    if db.get_by_id(id=id) is None:
        raise HTTPException(status_code=400, detail="id does not exists")
    resp = db.delete(id=id)
    return DelNewsOut.from_orm(resp)
