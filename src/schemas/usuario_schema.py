from marshmallow import Schema, fields,validate
from src.models.usuario_model import UsuarioModel
from src.common.utils import ma

class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UsuarioModel
        load_instance = True
        ordered = True

class UsuarioSchemaValidar(Schema):
    IDUSUARIO = fields.Int(required=True)
    NOMBRE = fields.Str(required=True)
    APELLIDO = fields.Str(required=True)
    EDAD = fields.Int(required=True, validate= validate.Range(1,99))
    CORREO = fields.Str(required=True)
    PASSWORD = fields.Str(required=True)

class UsuarioSchemaLogin(Schema):
    CORREO = fields.Str(required=True)
    PASSWORD = fields.Str(required=True)