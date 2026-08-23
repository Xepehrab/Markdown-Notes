# md-notes-api

A FastAPI-based Markdown note-taking API with save/list/render endpoints, file upload, and grammar checking — built as a learning project following the [roadmap.sh](https://roadmap.sh/projects/markdown-note-taking-app) guide.

## Features

- Save and list notes (stored in `notes.json`)
- Each note gets a unique `uuid` id
- Render Markdown text to HTML
- Render a saved note to HTML by its id
- Upload a `.md` file and store its content
- Grammar check (English, via LanguageTool)

## Requirements

- Python 3.9+
- Java (required by `language_tool_python`)
- pip packages: `fastapi`, `uvicorn`, `markdown`, `language-tool-python`

## Install

