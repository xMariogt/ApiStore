from flask_jwt_extended import jwt_required
from src.models.metodo_model import MetodoModel
from src.schemas.metodo_schema import MetodoSchema, MetodoSchemaValidar
from src.common.utils import db, api
from sqlalchemy.exc import NoResultFound
from marshmallow import ValidationError
from flask_restx import Resource
from flask import request
from src.swagger.metodo_swagger import MetodoSwagger

class MetodoController(Resource):
    @api.doc(description="Obtiene todos los Metodos")
    @api.response(200, "Devuelve un array de Metodos", MetodoSwagger, as_list=True)
    @api.response(401, "Token invalido")
    @api.response(503, "Algo salio mal, intenta de nuevo.")
    @jwt_required() 
    def get(self):
        try:
            metodosdb = MetodoModel.query.all()

            return MetodoSchema(many=True).dump(metodosdb), 200
        
        except Exception as e:
            return {"message": f"Algo ha salido mal con los metodos {e}"}, 503

    @api.doc(description="Agrega un Metodo")
    @api.expect(MetodoSwagger)
    @api.response(200, "Devuelve el Metodo insertado", MetodoSwagger)
    @api.response(401, "Token invalido")    
    @api.response(422, "Error de validacion")    
    @api.response(503, "Algo salio mal, intenta de nuevo.")
    @jwt_required()     
    def post(self):
        try:

            metodo = MetodoSchemaValidar().load(request.json)

            metodo = MetodoSchema(transient=True).load(request.json)

            db.session.add(metodo)
            db.session.commit()

            return MetodoSchema().dump(metodo), 201
        
        except ValidationError as err:
            return err.messages, 422
        except Exception as e:
            return {"message": f"Algo ha salido mal con los metodos {e}"}, 503

    @api.doc(description="Actualiza los datos de un metodo")
    @api.expect(MetodoSwagger)
    @api.response(200, "Devuelve el metodo actualizado", MetodoSwagger)
    @api.response(401, "Token invalido")
    @api.response(422, "Error de validacion.") 
    @api.response(404, "Categoria no encontrada.")   
    @api.response(503, "Algo salio mal, intenta de nuevo.")
    @jwt_required()     
    def put(self):
        try:

            metodo = MetodoSchemaValidar().load(request.json)
            metodo = MetodoSchema(transient=True).load(request.json)

            metododb = MetodoModel.query.where(MetodoModel.IDMETODO == metodo.IDMETODO).one()
            metododb.NOMBRE = metodo.NOMBRE

            db.session.commit()

            return MetodoSchema().dump(metododb), 200
        
        except NoResultFound as e:
            return {"msg": f"El metodo indicado no fue encontrado o no existe. {e}"}, 404
        except ValidationError as err:
            return err.messages, 422
        except Exception as e:
            return {"message": f"Algo ha salido mal con los metodos {e}"}, 503
        
class MetodoControllerById(Resource):
    @api.doc(description="Obtiene un Metodo por su ID")
    @api.response(200, "Devuelve el metodo hallado", MetodoSwagger)
    @api.response(401, "Token invalido")
    @api.response(404, "Metodo no encontrado.")   
    @api.response(503, "Algo salio mal, intenta de nuevo.")
    @jwt_required() 
    def get(self, idmetodo):
        try:
            metododb = MetodoModel.query.where(MetodoModel.IDMETODO == idmetodo).one()

            return MetodoSchema().dump(metododb), 200
        
        except NoResultFound as e:
            return {"msg": f"El metodo indicado no fue encontrado o no existe. {e}"}, 404
        except Exception as e:
            return {"message": f"Algo ha salido mal con los metodos {e}"}, 503

    @api.doc(description="Elimina un Metodo por su ID")
    @api.response(200, "Devuelve un mensaje de confirmacion.")
    @api.response(401, "Token invalido")
    @api.response(404, "Metodo no encontrado.")   
    @api.response(503, "Algo salio mal, intenta de nuevo.")
    @jwt_required()     
    def delete(self, idmetodo):
        try:
            metododb = MetodoModel.query.where(MetodoModel.IDMETODO == idmetodo).one()

            db.session.delete(metododb)
            db.session.commit()

            return {"msg": "Metodo eliminado correctamente."}, 200
        
        except NoResultFound as e:
            return {"msg": f"El metodo indicado no fue encontrado o no existe. {e}"}, 404
        except Exception as e:
            return {"message": f"Algo ha salido mal con los metodos {e}"}, 503

