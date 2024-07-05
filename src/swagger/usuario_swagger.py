from src.common.utils import api
from flask_restx import fields

UsuarioSwagger = api.model("UsuarioSwagger",{
    "IDUSUARIO": fields.Integer,
    "NOMBRE": fields.String,
    "APELLIDO": fields.String,
    "EDAD": fields.Integer,
    "CORREO": fields.String,
    "PASSWORD": fields.String,
})

UsuarioSwaggerPost = api.model("UsuarioSwaggerPost",{
    "NOMBRE": fields.String,
    "APELLIDO": fields.String,
    "EDAD": fields.Integer,
    "CORREO": fields.String,
    "PASSWORD": fields.String,
})

LoginSwagger = api.model("LoginSwagger",{
    "CORREO": fields.String,
    "PASSWORD": fields.String,
})

UsuarioSwaggerSecure = api.model("UsuarioSwagger",{
    "IDUSUARIO": fields.Integer,
    "NOMBRE": fields.String,
    "APELLIDO": fields.String,
    "EDAD": fields.Integer,
    "CORREO": fields.String,
})

