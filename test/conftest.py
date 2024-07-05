from app import app
import pytest

@pytest.fixture()
def client():
    client = app.test_client()

    yield client

@pytest.fixture()
def header(client):
    response = client.post("/api/store1.0/usuario/login", json={
        "CORREO": "admin@gmail.com",
        "PASSWORD": "admin123"
    })

    token = response.json['token']
    header = {"Authorization": f"Bearer {token}"}

    yield header