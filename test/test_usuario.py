
def test_getUsuarios(client, header):
    response = client.get("/api/store1.0/usuario", headers=header)

    assert response.status_code == 200

def test_addUsuario(client, header):
    response = client.post("/api/store1.0/usuario", json={
        "NOMBRE": "usuario1",
        "APELLIDO": "PRUEBA",
        "EDAD": 21,
        "CORREO": "prueba@gmail.com",
        "PASSWORD": "123456"
    }, headers= header)

    assert response.status_code == 201

def test_updateUsuario(client, header):
    response = client.put("/api/store1.0/usuario", json={
        "IDUSUARIO": 1,
        "NOMBRE": "usuario1",
        "APELLIDO": "PRUEBA2",
        "EDAD": 21,
        "CORREO": "prueba@gmail.com",
        "PASSWORD": "123456"
    }, headers=header)

    assert response.status_code == 200

#PRUEBAS CON ID DE USUARIO

idusuario = 1

def test_getOneUsuario(client, header):
    response = client.get(f"/api/store1.0/usuario/idusuario/{idusuario}", headers=header)

    assert response.status_code == 200

'''
def test_deleteUsuario(client, header):
    response = client.delete(f"/api/store1.0/usuario/idusuario/{idusuario}", headers=header)

    assert response.status_code == 200
'''
