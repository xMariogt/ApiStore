from src.common.utils import ma
from marshmallow import Schema, fields
from src.models.pedido_model import PedidoModel

class PedidoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PedidoModel
        load_instance = True
        ordered = True
        include_fk = True
        include_relationships=True

    #Relationships
    USUARIO = fields.Nested("UsuarioSchema", exclude=["PASSWORD",])

class PedidoSchemaValidar(Schema):
    IDPEDIDO = fields.Int(required= True)
    FECHA_PEDIDO = fields.DateTime(required=True)
    TOTAL = fields.Float(required=True)
    CANTIDAD = fields.Int(required=True)
    IDUSUARIO = fields.Int(required= True) 
    IDPRODUCTO = fields.Int(required= True)
    IDMETODO = fields.Int(required= True)