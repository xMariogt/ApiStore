from flask_restx import fields
from src.common.utils import api
from src.swagger.usuario_swagger import UsuarioSwaggerSecure
PedidoSwagger = api.model("PedidoSwagger", {
    "IDPEDIDO": fields.Integer,
    "FECHA_PEDIDO": fields.DateTime,
    "TOTAL": fields.Float,
    "CANTIDAD": fields.Integer,
    "IDUSUARIO": fields.Integer,
    "IDPRODUCTO": fields.Integer,
    "IDMETODO": fields.Integer
})

PedidoSwaggerPost = api.model("PedidoSwaggerPost", {
    "FECHA_PEDIDO": fields.DateTime,
    "CANTIDAD": fields.Integer,
    "IDUSUARIO": fields.Integer,
    "IDPRODUCTO": fields.Integer,
    "IDMETODO": fields.Integer
})

PedidoSwaggerUsuario = api.model("PedidoSwaggerUsuario", {
    "IDPEDIDO": fields.Integer,
    "FECHA_PEDIDO": fields.DateTime,
    "TOTAL": fields.Float,
    "CANTIDAD": fields.Integer,
    "IDUSUARIO": fields.Integer,
    "IDPRODUCTO": fields.Integer,
    "IDMETODO": fields.Integer,
    "USUARIO": fields.Nested(UsuarioSwaggerSecure, as_list=True)
})