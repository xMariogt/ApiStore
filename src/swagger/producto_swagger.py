from flask_restx import fields
from src.common.utils import api

ProductoSwagger = api.model("ProductoSwagger", {
    "IDPRODUCTO": fields.Integer,
    "NOMBRE": fields.String,
    "DESCRIPCION": fields.String,
    "PRECIO": fields.Float,
    "STOCK": fields.Integer,
    "IDCATEGORIA": fields.Integer,
})

ProductoSwaggerPost = api.model("ProductoSwaggerPost",{
    "NOMBRE": fields.String,
    "DESCRIPCION": fields.String,
    "PRECIO": fields.Float,
    "STOCK": fields.Integer,
    "IDCATEGORIA": fields.Integer,
})