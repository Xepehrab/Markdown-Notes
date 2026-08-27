# Markdown

A FastAPI-based Markdown note-taking API with save/list/render endpoints, file upload, and grammar checking — built as a learning project following the [roadmap.sh](https://roadmap.sh/projects/markdown-note-taking-app) guide.

## Features

- Save and list notes (stored in `notes.json`)
- Each note gets a unique UUID `id` (string)
- Render Markdown text to HTML
- Render a saved note to HTML by its id
- Upload a `.md` file and store its content
- Grammar check (English, via LanguageTool)
- Clean code with `ruff` linting + auto-format
- Error handling & logging on file operations


## Project structure

```
markdown/
├── app/
│   ├── main.py              # FastAPI app and router wiring
│   ├── models.py            # Pydantic models (Item, TextPayload)
│   ├── storage.py           # JSON file read/write for notes
│   ├── routes/
│   │   ├── items.py         # CRUD, upload, health check
│   │   ├── render.py        # Markdown → HTML
│   │   └── grammar.py       # Grammar check endpoint
│   └── services/
│       ├── markdown.py      # Markdown rendering logic
│       └── grammar.py       # LanguageTool wrapper
├── main.py                  # Entry point (re-exports app)
├── notes.json               # Note storage (created at runtime)
├── requirements.txt
├── test_app.py              # Automated tests
└── README.md
```

## Requirements

- Python 3.9+
- Java (required by `language-tool-python`)
- ruff (for linting)

## Linting

bash
pip install ruff
ruff check .
ruff format .

## Install

```bash
pip install -r requirements.txt
```

## Run

From the project root:

```bash
uvicorn main:app --reload
```

Or:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`. Interactive docs at `/docs`.

## API endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/hello` | Health check |
| POST | `/items` | Create a note |
| GET | `/items` | List notes (`?limit=10`) |
| GET | `/items/{item_id}` | Get one note by UUID |
| POST | `/render` | Render Markdown text to HTML |
| GET | `/items/{item_id}/html` | Render a saved note to HTML |
| POST | `/upload` | Upload a `.md` file as a new note |
| POST | `/check-grammar` | Check English grammar |

### Example requests

Create a note:

```bash
curl -X POST http://127.0.0.1:8000/items \
  -H "Content-Type: application/json" \
  -d '{"text": "# Hello\n\nThis is **markdown**.", "is_done": false}'
```

Render Markdown:

```bash
curl -X POST http://127.0.0.1:8000/render \
  -H "Content-Type: application/json" \
  -d '{"text": "# Hello"}'
```

Check grammar:

```bash
curl -X POST http://127.0.0.1:8000/check-grammar \
  -H "Content-Type: application/json" \
  -d '{"text": "This are wrong."}'
```
