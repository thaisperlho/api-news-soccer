from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel, Field 
from typing import List
from db import insert

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
def read_item(item_id: int):
    global items
    for item in items:
        if item.id == item_id:
            return item
    return None

@app.put("/items/{item_id}", response_model=ItemOut)
def update_item(item_id: int, item: Item):
    global items
    for it in items:
        if it.id == item_id:
            it.name = item.name
            it.price = item.price
            it.is_offer = item.is_offer
            return it
    return None

@app.delete("/items/{item_id}", response_model=ItemOut)
def delete_item(item_id: int):
    global items
    for index in range(len(items)):
        if items[index].id == item_id:
            return items.pop(index)
    return None

