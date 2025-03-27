from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_open_calculator():
    response = client.post("/execute", json={"prompt": "Launch calculator"})
    assert response.status_code == 200
    assert "open_calculator" in response.json()["function"]
