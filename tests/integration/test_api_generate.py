from fastapi.testclient import TestClient
from backend.main import app


def test_api_generate_returns_story():
    client = TestClient(app)
    response = client.post("/story/generate", json={"prompt": "A moonlit shrine."})
    assert response.status_code == 200
    assert response.json()["title"] == "Untitled Yugen Tale"
