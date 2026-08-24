from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse

from app.models import TextPayload
from app.services.markdown import render
from app.storage import read_items

router = APIRouter(tags=["render"])


@router.post("/render")
def render_markdown(payload: TextPayload):
    return HTMLResponse(render(payload.text))


@router.get("/items/{item_id}/html")
def html_markdown(item_id: str):
    items = read_items()
    item = next((i for i in items if i["id"] == item_id), None)
    if item:
        return HTMLResponse(render(item["text"]))
    raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
