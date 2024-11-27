from fastapi.testclient import TestClient
from app import app, CountWordRequest, CountWordResponse

client = TestClient(app)

def test_hello():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_count_words():
    request = CountWordRequest(text="hello world")
    response = client.post("/count_words", json=request.model_dump())
    assert response.status_code == 200
    assert response.json() == {"count": 2, "words": ["hello", "world"]}
    
