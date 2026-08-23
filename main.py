from fastapi import FastAPI, HTTPException, UploadFile , File
from pydantic import BaseModel
import json
import os
import markdown
from fastapi.responses import HTMLResponse
import uuid
import language_tool_python

app = FastAPI()

class Item(BaseModel):
    id : str
    text: str
    is_done: bool = False

NOTES_FILE = "notes.json"

def read_items():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def write_items(items):
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)

@app.get('/hello')
def say_ok():
    return {"message": "Ok"}

@app.post("/items")
def create_items(item: Item):
    items = read_items()
    item.id=int(uuid.uuid4())
    items.append(item.model_dump())
    write_items(items)
    return items

@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    items = read_items()
    return items[0:limit]

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    items = read_items()
    item= next((i for i in items if i["id"]== item_id),None)
    if item:
        return item
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")

@app.post("/render")
def render_markdown(payload: dict):
    html1=markdown(payload["text"])
    return HTMLResponse(html1)

@app.get("/items/{item_id}/html")
def html_markdown(item_id:str):
    items= read_items()
    item = next((i for i in items if i['id']== item_id),None)
    if item:
        html1=markdown(item['text'])
        return HTMLResponse(html1)
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")


@app.post("/upload")
async def upload_file(file: UploadFile=File(...)):
    content= await file.read()
    text= content.decode("utf-8")

    items= read_items()
    new_item = {                        
        "id": str(uuid.uuid4()),         
        "text": text,                   
        "is_done": False
    }
    items.append(new_item)               
    write_items(items)               
    return new_item     

tool = language_tool_python.LanguageTool("en-US")

@app.post("/check-grammar")
def check_grammar(payload: dict):
    matches = tool.check(payload["text"])
    mistakes = []
    for m in matches:
        mistakes.append({
            "message": m.message,
            "suggestions": m.replacements,
            "offset": m.offset,
            "length": m.error_length,
        })
    return mistakes
