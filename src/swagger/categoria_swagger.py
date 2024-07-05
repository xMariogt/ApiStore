from src.common.utils import api
from flask_restx import fields

CategoriaSwagger = api.model("CategoriaSwagger", {
    "IDCATEGORIA": fields.Integer,
    "NOMBRE": fields.String,
})