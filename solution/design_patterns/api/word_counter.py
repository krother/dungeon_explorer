"""
Word counter business logic

also see:
   BCE Pattern : Behavior Controller Entity
   (Robert C. Martin - Uncle Bob)
"""
from pydantic import BaseModel

# data exchange objects
class CountWordRequest(BaseModel):
    text: str

class CountWordResponse(BaseModel):
    count: int
    words: list[str]


def count_words(request: CountWordRequest) -> CountWordResponse:
    words = request.text.split()
    return CountWordResponse(
        count = len(words),
        words = words,
    )