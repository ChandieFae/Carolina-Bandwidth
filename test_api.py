## tests/test_api.py
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Carolina Bandwidth is live"}


def test_text_endpoint():
    response = client.post("/text", json={"input_text": "Hello"})
    assert response.status_code == 200

