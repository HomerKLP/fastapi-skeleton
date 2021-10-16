from fastapi.testclient import TestClient

from main import app

client: TestClient = TestClient(app=app)


def test_health_check() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "ok"
