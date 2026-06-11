from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool = True

class ItemResponse(Item):
    id: int

items = []
next_id = 1

@app.get("/items/{item_id}", response_model=ItemResponse)
def read_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items", response_model=ItemResponse, status_code=201)
def create_item(item: Item):
    global next_id
    new_item = item.dict()
    new_item["id"] = next_id
    next_id += 1
    items.append(new_item)
    return new_item

# Example usage:
# POST /items with JSON body:
# {
#   "name": "Notebook",
#   "description": "A spiral-bound notebook",
#   "price": 4.99,
#   "in_stock": true
# }
# Then GET /items/1 to retrieve the created item.
