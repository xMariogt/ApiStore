from flask_jwt_extended import jwt_required
from src.common.utils import db, api
from src.models.producto_model import ProductoModel
from src.schemas.producto_schema import ProductoSchema, ProductoSchemaValidar
from src.swagger.producto_swagger import ProductoSwagger, ProductoSwaggerPost
from sqlalchemy.exc import NoResultFound
from marshmallow import ValidationError
from flask_restx import Resource
from flask import request


class ProductoController(Resource):
    @api.doc(description="Obtiene todos los Productos")
    @api.response(200, "Devuelve un array de Productos", ProductoSwagger, as_list=True)
    @api.response(401, "Token invalido")
    @api.response(503, "Algo salio mal, intenta de nuevo.")
    @jwt_required() 
    def get(self):
        try:

            productodb = ProductoModel.query.all()

            return ProductoSchema(many=True).dump(productodb), 200
        
        except Exception as e:
            return {"msg": f"Algo ha salido mal con los productos {e}"}, 503

    @api.doc(description="Agrega un producto")
    @api.expect(ProductoSwaggerPost)
    @api.response(200, "Devuelve el producto insertado", ProductoSwagger)
    @api.response(401, "Token invalido")
    @api.response(422, "Error de validacion")    
    @api.response(503, "Algo salio mal, intenta de nuevo.")
    @jwt_required()     
    def post(self):
        try:

            producto = ProductoSchemaValidar(exclude=["IDPRODUCTO",]).load(request.json)
            producto = ProductoSchema(transient=True).load(request.json)

            db.session.add(producto)
            db.session.commit()

            return ProductoSchema().dump(producto), 201
        
        except ValidationError as err:
            return err.messages, 422
        except Exception as e:
            return {"msg": f"Algo ha salido mal con los productos {e}"}, 503

    @api.doc(description="Actualiza los datos de un producto")
    @api.expect(ProductoSwagger)
    @api.response(200, "Devuelve el producto actualizado", ProductoSwagger)
    @api.response(401, "Token invalido")
    @api.response(422, "Error de validacion.") 
    @api.response(404, "Producto no encontrado.")   
    @api.response(503, "Algo salio mal, intenta de nuevo.")
    @jwt_required()     
    def put(self):
        try:

            producto = ProductoSchemaValidar().load(request.json)
            producto = ProductoSchema(transient=True).load(request.json)

            productodb = ProductoModel.query.where(ProductoModel.IDPRODUCTO == producto.IDPRODUCTO).one()

            productodb.NOMBRE = producto.NOMBRE
            productodb.PRECIO = producto.PRECIO
            productodb.STOCK = producto.STOCK

            db.session.commit()

            return ProductoSchema().dump(productodb)
        
        except NoResultFound as e:
            return {"msg": f"El producto indicado no fue encontrado o no existe. {e}"}, 404
        except ValidationError as err:
            return err.messages, 422
        except Exception as e:
            return {"msg": f"Algo ha salido mal con los productos {e}"}, 503
        
class ProductoControllerById(Resource):
    @api.doc(description="Obtiene un producto por su ID")
    @api.response(200, "Devuelve el producto hallado", ProductoSwagger)
    @api.response(401, "Token invalido")
    @api.response(404, "Producto no encontrado.")   
    @api.response(503, "Algo salio mal, intenta de nuevo.")
    @jwt_required() 
    def get(self, idproducto):
        try:
            productodb = ProductoModel.query.where(ProductoModel.IDPRODUCTO == idproducto).one()

            return ProductoSchema().dump(productodb)
        
        except NoResultFound as e:
            return {"msg": f"El producto indicado no fue encontrado o no existe. {e}"}, 404
        except Exception as e:
            return {"msg": f"Algo ha salido mal con los productos {e}"}, 503

    @api.doc(description="Elimina un producto por su ID")
    @api.response(200, "Devuelve un mensaje de confirmacion.")
    @api.response(401, "Token invalido")
    @api.response(404, "Producto no encontrado.")   
    @api.response(503, "Algo salio mal, intenta de nuevo.")
    @jwt_required()     
    def delete(self, idproducto):
        try:
            productodb = ProductoModel.query.where(ProductoModel.IDPRODUCTO == idproducto).one()

            db.session.delete(productodb)
            db.session.commit()

            return {"msg": "Producto eliminado correctamente"}, 200
        
        except NoResultFound as e:
            return {"msg": f"El producto indicado no fue encontrado o no existe. {e}"}, 404
        except Exception as e:
            return {"msg": f"Algo ha salido mal con los productos {e}"}, 503