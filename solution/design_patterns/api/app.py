import asyncio
import random
from fastapi import FastAPI
from word_counter import count_words, CountWordRequest, CountWordResponse

app = FastAPI()


@app.get("/")
async def hello():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str|None = None):
    return {"item_id": item_id, "q": q}


@app.post("/count_words")
async def count_words_endpoint(request: CountWordRequest) -> CountWordResponse:
    await asyncio.sleep(random.randint(5, 10))
    return count_words(request)
