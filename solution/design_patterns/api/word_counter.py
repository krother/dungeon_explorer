"""
Word counter business logic

also see:
   BCE Pattern : Behavior Controller Entity
   (Robert C. Martin - Uncle Bob)
"""
from pydantic import BaseModel
from functools import wraps

# data exchange objects
class CountWordRequest(BaseModel):
    text: str

class CountWordResponse(BaseModel):
    count: int
    words: list[str]

import time

def print_timestamp(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("before:", time.asctime())  # done before addition
        result = func(*args, **kwargs)   # calls the addition function
        print("after:", time.asctime())
        return result
    
    return wrapper


@print_timestamp
def count_words(request: CountWordRequest) -> CountWordResponse:
    words = request.text.split()
    return CountWordResponse(
        count = len(words),
        words = words,
    )

count_words(CountWordRequest(text="hello world"))

print(count_words)
print(count_words.__annotations__)
