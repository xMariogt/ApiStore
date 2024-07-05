from src.common.utils import api
from flask_restx import fields

MetodoSwagger = api.model("MetodoSwagger", {
    "IDMETODO": fields.Integer,
    "NOMBRE": fields.String,
})