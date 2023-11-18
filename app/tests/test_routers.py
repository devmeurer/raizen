from fastapi.testclient import TestClient
import pytest
from app.routers.views import app


@pytest.fixture(scope="module")
def client():
    return TestClient(app)

def test_get_weather(client: TestClient):
    city = "Lisbon"
    response = client.get(f"/weather/{city}")
    assert response.status_code == 200
    data = response.json()
    assert "city" in data
    assert "list" in data  # 'list' é um campo comum na resposta da API do OpenWeatherMap
