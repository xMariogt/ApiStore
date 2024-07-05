
def test_getPedidos(client, header):
    response = client.get("/api/store1.0/pedido", headers= header)

    assert response.status_code == 200

def test_postPedidos(client, header):
    response = client.post("/api/store1.0/pedido", headers= header, json={
        "FECHA_PEDIDO": "2021-10-10T12:00:00",
        "CANTIDAD": 1,
        "IDUSUARIO": 1,
        "IDPRODUCTO": 1,
        "IDMETODO": 1
    })

    assert response.status_code == 200

def test_putPedidos(client, header):
    response = client.put("api/store1.0/pedido", json={
        "IDPEDIDO": 1,
        "FECHA_PEDIDO": "2021-10-10 12:00:00",
        "CANTIDAD": 5,
        "TOTAL":4,
        "IDUSUARIO": 1,
        "IDPRODUCTO": 1,
        "IDMETODO": 1
    })

idusuario = 1

def test_getPedidosByUser(client, header):
    response = client.get(f"/api/store1.0/pedido/idusuario/{idusuario}", headers=header)

    assert response.status_code == 200

idpedido = 1

def test_getPedidoById(client, header):
    response = client.get(f"/api/store1.0/pedido/idusuario/{idusuario}", headers=header)

    assert response.status_code == 200