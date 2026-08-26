from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_hello():
    r = client.get("/hello")
    assert r.status_code == 200
    assert r.json() == {"message": "Ok"}

def test_create_and_get_item():
    # create
    r = client.post("/items", json={"text": "# سلام", "is_done": False})
    assert r.status_code == 200
    items = r.json()
    assert len(items) >= 1
    item_id = items[-1]["id"]
    # get by id
    r2 = client.get(f"/items/{item_id}")
    assert r2.status_code == 200
    assert r2.json()["text"] == "# سلام"

def test_render():
    r = client.post("/render", json={"text": "# Hi"})
    assert r.status_code == 200
    assert "<h1>Hi</h1>" in r.text

def test_render_saved_html():
    # create then render by id
    r = client.post("/items", json={"text": "**bold**", "is_done": False})
    item_id = r.json()[-1]["id"]
    r2 = client.get(f"/items/{item_id}/html")
    assert r2.status_code == 200
    assert "<strong>bold</strong>" in r2.text

def test_not_found():
    r = client.get("/items/does-not-exist-id")
    assert r.status_code == 404
