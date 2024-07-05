from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource
from marshmallow import ValidationError
from sqlalchemy.exc import NoResultFound
from src.models.producto_model import ProductoModel
from src.models.pedido_model import PedidoModel
from src.schemas.pedido_schema import PedidoSchema, PedidoSchemaValidar
from src.common.utils import db, api
from src.swagger.pedido_swagger import PedidoSwagger, PedidoSwaggerPost, PedidoSwaggerUsuario

class PedidoController(Resource):
    @api.doc(description="Obtiene todos los Pedidos")
    @api.response(200, "Devuelve un array de Pedidos", PedidoSwagger, as_list=True)
    @api.response(401, "Token invalido")
    @api.response(503, "Algo salio mal, intenta de nuevo.")
    @jwt_required()
    def get(self):
        try:
            pedido = PedidoModel.query.all()

            return PedidoSchema(many=True).dump(pedido), 200
        
        except Exception as e:
            return {"msg": f"Algo ha salido mal con los Pedidos {e}"}, 503
        
    @api.doc(description="Agrega un pedido")
    @api.expect(PedidoSwaggerPost)
    @api.response(200, "Devuelve el pedido  insertado", PedidoSwagger)
    @api.response(401, "Token invalido")
    @api.response(422, "Error de validacion")    
    @api.response(503, "Algo salio mal, intenta de nuevo.")
    @jwt_required()
    def post(self):
        try:
            #VALIDAMOS QUE LOS CAMPOS SOLICITADOS SEAN CORRECTOS
            pedidovalidar = PedidoSchemaValidar(exclude=["IDPEDIDO", "TOTAL"]).load(request.json)
            
            producto = ProductoModel.query.where(ProductoModel.IDPRODUCTO == pedidovalidar.get("IDPRODUCTO")).one()
            if producto.STOCK < pedidovalidar.get("CANTIDAD"):
                raise Exception
            else:
                #Guardamos el JSON en una nueva variable
                pedidoJSON = request.json
                #Se agrega el total al JSON que se recibio
                pedidoJSON["TOTAL"] = float(producto.PRECIO * pedidoJSON.get("CANTIDAD"))
                
                #aqui ya confirmamos que el nuevo objeto del nuevo pedido
                newpedido = PedidoSchema(transient=True).load(pedidoJSON)

                #db.session.begin()
                db.session.add(newpedido) #Agregamos el nuevo pedido a la bd
                db.session.flush()

                #Restamos la cantidad de productos al stock si el pedido es agregado
                producto.STOCK = producto.STOCK-pedidovalidar.get("CANTIDAD")
                db.session.commit()

                return PedidoSchema().dump(newpedido), 200

        except ValidationError as err:
            return err.messages, 422
        except NoResultFound as e:
            return {"msg": f"producto no encontrado {e}"},
        except Exception as e:
            db.session.rollback()
            return {"msg": f"Algo ha salido mal con los Pedidos {e}"}, 503
    
    @api.doc(description="Actualiza un pedido")
    @api.expect(PedidoSwagger)
    @api.response(200, "Devuelve el pedido actualizado", PedidoSwagger)
    @api.response(401, "Token invalid")
    @api.response(422, "Error de validacion")
    @api.response(404, "Pedido no encontrado.")
    @api.response(503, "Algo salio mal, intenta de nuevo.")
    @jwt_required()
    def put(self):
        try:
            #Se valida que la informacion venga adecuadamente
            pedido = PedidoSchemaValidar().load(request.json)
            pedido = PedidoSchema(transient=True).load(request.json)

            #Se busca el producto y el pedido en la base de datos
            productodb = ProductoModel.query.where(ProductoModel.IDPRODUCTO == pedido.IDPRODUCTO).one()
            pedidodb = PedidoModel.query.where(PedidoModel.IDPEDIDO == pedido.IDPEDIDO).one()

            #Si la cantidad nueva es mayor que la cantidad anterior, implica un aumento en el pedido
            if pedido.CANTIDAD > pedidodb.CANTIDAD:
                if productodb.STOCK > (pedido.CANTIDAD - pedidodb.CANTIDAD): #Se verifica que existan suficientes unidades extra
                    productodb.STOCK = productodb.STOCK - (pedido.CANTIDAD - pedidodb.CANTIDAD)#Se resta el extra de unidades del stock
                else:
                    raise Exception
            elif pedido.CANTIDAD < pedidodb.CANTIDAD: #Se verifica si la cantidad nueva es menor que la anterior, lo que implica una devolucion
                productodb.STOCK = productodb.STOCK + (pedidodb.CANTIDAD - pedido.CANTIDAD) #Se suma la cantidad regresada al stock

            #Se hacen elresto de modificaciones
            pedidodb.FECHA_PEDIDO = pedido.FECHA_PEDIDO            
            pedidodb.CANTIDAD = pedido.CANTIDAD
            pedidodb.TOTAL = pedido.CANTIDAD * productodb.PRECIO #El total debe cambiar si la cantidad subio o bajo

            db.session.commit()

            return PedidoSchema().dump(pedidodb), 200
        
        except ValidationError as err:
            return err.messages, 422
        except NoResultFound as e:
            return {"msg": f"Pedido no encontrado {e}"}, 404
        except Exception as e:
            return {"msg": f"Algo ha salido mal con los Pedidos {e}"}, 503
        

class PedidoControllerByUser(Resource):
    @api.doc(description="Obtiene los pedidos por ID de Usuario")
    @api.response(200, "Devuelve el producto hallado", PedidoSwaggerUsuario)
    @api.response(401, "Token invalido")
    @api.response(404, "Pedido no encontrado.")   
    @api.response(503, "Algo salio mal, intenta de nuevo.")
    @jwt_required()
    def get(self, idusuario):
        try:
            pedidos_usuario = PedidoModel.query.where(PedidoModel.IDUSUARIO == idusuario).all()

            return PedidoSchema(many=True).dump(pedidos_usuario), 200
        
        except Exception as e:
            return {"msg": f"Algo ha salido mal con los Pedidos {e}"}, 503
        
class PedidoControllerById(Resource):
    @api.doc(description="Obtiene un pedido por su ID")
    @api.response(200, "Devuelve el producto hallado", PedidoSwagger)
    @api.response(401, "Token invalido")
    @api.response(404, "Pedido no encontrado.")   
    @api.response(503, "Algo salio mal, intenta de nuevo.")
    @jwt_required()
    def get(self, idpedido):
        try:
            pedido = PedidoModel.query.where(PedidoModel.IDPEDIDO == idpedido).one()

            return PedidoSchema().dump(pedido), 200
        
        except NoResultFound as e:
            return {"msg": f"Pedido no encontrado {e}"}, 404
        except Exception as e:
            return {"msg": f"Algo ha salido mal con los Pedidos {e}"}, 503
        
    @jwt_required()
    @api.doc(description="Elimina un pedido por su ID")
    @api.response(200, "Devuelve un mensaje de confirmacion.")
    @api.response(401, "Token invalido")
    @api.response(404, "Pedido no encontrado.")   
    @api.response(503, "Algo salio mal, intenta de nuevo.")
    def delete(self, idpedido):
        try:
            pedido = PedidoModel.query.where(PedidoModel.IDPEDIDO == idpedido).one()

            db.session.delete(pedido)

            db.session.commit()

            return {"msg": "Pedido eliminado"}, 200
        
        except NoResultFound as e:
            return {"msg": f"Pedido no encontrado {e}"}, 404
        except Exception as e:
            return {"msg": f"Algo ha salido mal con los Pedidos {e}"}, 503