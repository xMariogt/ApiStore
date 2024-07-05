from app import app

def test_login():
    client = app.test_client()

    response = client.post("/api/store1.0/usuario/login", json={
        "CORREO": "admin@gmail.com",
        "PASSWORD": "admin123"
    })

    assert response.status_code == 200