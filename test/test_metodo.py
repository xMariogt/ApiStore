
def test_getmetodos(client, header):
    response = client.get("/api/store1.0/metodo", headers=header)

    assert response.status_code == 200

def test_addmetodo(client, header):
    response = client.post("/api/store1.0/metodo", json={
        "IDMETODO": 1,
        "NOMBRE": "Prueba"
    },headers=header)

    assert response.status_code == 201

def test_updatemetodo(client, header):
    response = client.put("/api/store1.0/metodo", json={
        "IDMETODO": 1,
        "NOMBRE": "Prueba2"
    },headers=header)

    assert response.status_code == 200


#Pruebas de metodos con idmetodos
idmetodo = 1

def test_getOnemetodo(client, header):
    response = client.get(f"/api/store1.0/metodo/idmetodo/{idmetodo}", headers=header)

    assert response.status_code == 200