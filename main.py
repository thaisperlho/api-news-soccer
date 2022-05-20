from datetime import datetime
from turtle import up
from fastapi import FastAPI
from pydantic import BaseModel, Field 
from typing import List
from db import insert, select, update

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class ItemOut(Item):
    id: int

items: List[ItemOut] = []
id = 1

@app.post("/items", response_model=ItemOut)
def post_item(item: Item):
    id = insert(
        name=item.name, 
        price=item.price, 
        is_offer=item.is_offer, 
        created_at=item.created_at, 
        updated_at=item.updated_at)
    data = item.dict()
    data.update({"id": id})
    out = ItemOut(**data)
    return out

@app.get("/items/{item_id}", response_model=ItemOut)
def get_item(item_id: int):
    data = select(id=item_id)
    if not data:
        return None
    item = ItemOut(name=data[1],price=data[2],is_offer=data[3],created_at=data[4],updated_at=data[5],id=data[0])
    return item

@app.put("/items/{item_id}", response_model=ItemOut)
def put_item(item_id: int, item: Item):
    value = select(id=item_id)
    if not value:
        return None
    update(name=item.name, 
        price=item.price, 
        is_offer=item.is_offer,  
        updated_at=item.updated_at,
        id=item_id)
    data = item.dict()
    data.update({"id": item_id})
    out = ItemOut(**data)
    return out

@app.delete("/items/{item_id}", response_model=ItemOut)
def delete_item(item_id: int):
    global items
    for index in range(len(items)):
        if items[index].id == item_id:
            return items.pop(index)
    return None

