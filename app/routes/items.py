import uuid

from fastapi import APIRouter, HTTPException, UploadFile

from app.models import Item
from app.storage import read_items, write_items

router = APIRouter(tags=["items"])


@router.get("/hello")
def say_ok():
    return {"message": "Ok"}


@router.post("/items")
def create_items(item: Item):
    items = read_items()
    item.id = str(uuid.uuid4())
    items.append(item.model_dump())
    write_items(items)
    return items


@router.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    items = read_items()
    return items[0:limit]


@router.get("/items/{item_id}", response_model=Item)
def get_item(item_id: str) -> Item:
    items = read_items()
    item = next((i for i in items if i["id"] == item_id), None)
    if item:
        return item
    raise HTTPException(status_code=404, detail=f"Item {item_id} not found")


@router.post("/upload")
async def upload_file(file: UploadFile):
    content = await file.read()
    text = content.decode("utf-8")

    items = read_items()
    new_item = {
        "id": str(uuid.uuid4()),
        "text": text,
        "is_done": False,
    }
    items.append(new_item)
    write_items(items)
    return new_item

