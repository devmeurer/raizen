from io import BytesIO

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.database.config import get_db
from app.routers.views import app


@pytest.fixture(scope="module")
def client():
    return TestClient(app)


def test_create_product_csv(client: TestClient):
    response = client.post(
        "/products/upload",
        data={
            "file": (
                BytesIO(
                    b"name,description,price,quantity\nprod1,desc1,10,5\nprod2,desc2,20,10"
                ),
                "products.csv",
            )
        },
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Dados inseridos com sucesso"}


def test_create_product(client: TestClient):
    response = client.post(
        "/products/",
        json={"name": "prod1", "description": "desc1", "price": 10, "quantity": 5},
    )
    assert response.status_code == 200


def test_read_product(client: TestClient):
    response = client.get("/products/1")
    assert response.status_code == 200


def test_read_product_not_found(client: TestClient):
    response = client.get("/products/2000")
    assert response.status_code == 500


def test_update_product(client: TestClient):
    response = client.put(
        "/products/1",
        json={
            "name": "prod1_updated",
            "description": "desc1_updated",
            "price": 15,
            "quantity": 10,
        },
    )
    assert response.status_code == 200
    assert response.json() == {"id": 1, "message": "Produto atualizado com sucesso"}


def test_delete_product(client: TestClient):
    response = client.delete("/product/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Produto excluído com sucesso"}


def test_delete_product_not_found(client: TestClient):
    response = client.delete("/product/2")
    assert response.status_code == 200
    assert response.json() == {"message": "Produto não encontrado"}
