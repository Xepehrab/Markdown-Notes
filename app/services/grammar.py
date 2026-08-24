import language_tool_python

_tool: language_tool_python.LanguageTool | None = None


def _get_tool() -> language_tool_python.LanguageTool:
    global _tool
    if _tool is None:
        _tool = language_tool_python.LanguageTool("en-US")
    return _tool


def check_grammar(text: str) -> list[dict]:
    matches = _get_tool().check(text)
    return [
        {
            "message": m.message,
            "suggestions": m.replacements,
            "offset": m.offset,
            "length": m.error_length,
        }
        for m in matches
    ]
