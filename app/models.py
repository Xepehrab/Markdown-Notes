from pydantic import BaseModel


class Item(BaseModel):
    id: str = ""
    text: str
    is_done: bool = False


class TextPayload(BaseModel):
    text: str
