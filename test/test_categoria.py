
def test_getCategorias(client, header):
    response = client.get("/api/store1.0/categoria", headers=header)

    assert response.status_code == 200

def test_addCategoria(client, header):
    response = client.post("/api/store1.0/categoria", json={
        "IDCATEGORIA": 1,
        "NOMBRE": "Prueba"
    },headers=header)

    assert response.status_code == 201

def test_updateCategoria(client, header):
    response = client.put("/api/store1.0/categoria", json={
        "IDCATEGORIA": 1,
        "NOMBRE": "Prueba2"
    },headers=header)

    assert response.status_code == 200


#Pruebas de metodos con idmetodos
idcategoria = 1

def test_getOneCategoria(client, header):
    response = client.get(f"/api/store1.0/categoria/idcategoria/{idcategoria}", headers=header)

    assert response.status_code == 200