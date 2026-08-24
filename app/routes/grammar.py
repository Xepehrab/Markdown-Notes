from fastapi import APIRouter

from app.models import TextPayload
from app.services.grammar import check_grammar

router = APIRouter(tags=["grammar"])


@router.post("/check-grammar")
def check_grammar_endpoint(payload: TextPayload):
    return check_grammar(payload.text)
