from src.common.utils import ma
from src.models.categoria_model import CategoriaModel
from marshmallow import Schema, fields

class CategoriaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= CategoriaModel
        ordered= True
        load_instance= True

class CategoriaSchemaValidar(Schema):
    IDCATEGORIA = fields.Int(required= True)
    NOMBRE = fields.Str(required= True)