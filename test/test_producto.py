
def test_getProductos(client, header):
    response = client.get("api/store1.0/producto", headers=header)

    assert response.status_code == 200

def test_addProducto(client, header):
    response = client.post("api/store1.0/producto", json={
        "NOMBRE": "Prueba",
        "DESCRIPCION": "Prueba",
        "PRECIO": 1.0,
        "STOCK": 1,
        "IDCATEGORIA": 1
    }, headers=header)

    assert response.status_code == 201

def test_updateProducto(client, header):
    response = client.put("api/store1.0/producto", json={
        "IDPRODUCTO": 1,
        "NOMBRE": "Prueba2",
        "DESCRIPCION": "Prueba2",
        "PRECIO": 2.0,
        "STOCK": 20,
        "IDCATEGORIA": 1
    }, headers=header)

    assert response.status_code == 200

idproducto = 1

def test_getOneProducto(client, header):
    response = client.get(f"api/store1.0/producto/idproducto/{idproducto}", headers=header)

    assert response.status_code == 200