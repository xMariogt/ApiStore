from src.models.producto_model import ProductoModel
from src.common.utils import ma
from marshmallow import Schema, fields, validate


class ProductoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductoModel
        load_instance = True
        ordered = True
        include_fk = True

class ProductoSchemaValidar(Schema):
    IDPRODUCTO = fields.Int(required=True)
    NOMBRE = fields.Str(required=True)
    DESCRIPCION = fields.Str(required=True)
    PRECIO = fields.Float(required=True)
    STOCK = fields.Int(required=True)
    IDCATEGORIA = fields.Int(required=True)