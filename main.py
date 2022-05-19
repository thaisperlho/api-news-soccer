from unicodedata import name
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
app = FastAPI()



class Item(BaseModel)
    name: str
    price: float
    is_offer: bool = None

class ItemOut(Item):
    id: int

items: List[ItemOut] = []
id = 1

@app.post("/items", response_model=ItemOut)
def post_item(item: Item):
    global id, items
    data = item.dict()
    data.update({"id": id})
    id += 1
    out = ItemOut(**data)
    items.append(out)
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

