from fastapi import FastAPI

from app.routes import grammar, items, render

app = FastAPI(title="md-notes-api")

app.include_router(items.router)
app.include_router(render.router)
app.include_router(grammar.router)
