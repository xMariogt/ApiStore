from src.common.utils import ma
from src.models.metodo_model import MetodoModel
from marshmallow import Schema, fields

class MetodoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= MetodoModel
        ordered= True
        load_instance= True

class MetodoSchemaValidar(Schema):
    IDMETODO = fields.Int(required= True)
    NOMBRE = fields.Str(required= True)