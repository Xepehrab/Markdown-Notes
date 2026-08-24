import markdown as md


def render(text: str) -> str:
    return md.markdown(text)
