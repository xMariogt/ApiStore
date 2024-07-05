from flask_jwt_extended import jwt_required
from src.models.categoria_model import CategoriaModel
from src.schemas.categoria_schema import CategoriaSchema, CategoriaSchemaValidar
from src.common.utils import db, api
from sqlalchemy.exc import NoResultFound
from marshmallow import ValidationError
from flask_restx import Resource
from flask import request
from src.swagger.categoria_swagger import CategoriaSwagger

class CategoriaController(Resource):
    @api.doc(description="Obtiene todas las Categorias")
    @api.response(200, "Devuelve un array de Categorias", CategoriaSwagger, as_list=True)
    @api.response(401, "Token invalido")
    @api.response(503, "Algo salio mal, intenta de nuevo.")
    @jwt_required()
    def get(self):
        try:
            categoriasdb = CategoriaModel.query.all()

            return CategoriaSchema(many=True).dump(categoriasdb), 200
        
        except Exception as e:
            return {"message": f"Algo ha salido mal con los categorias {e}"}, 503
        
    @api.doc(description="Agrega una Categoria")
    @api.expect(CategoriaSwagger)
    @api.response(200, "Devuelve la categoria insertada", CategoriaSwagger)
    @api.response(401, "Token invalido")    
    @api.response(422, "Error de validacion")    
    @api.response(503, "Algo salio mal, intenta de nuevo.")
    @jwt_required()    
    def post(self):
        try:

            categoria = CategoriaSchemaValidar().load(request.json)
            categoria = CategoriaSchema(transient=True).load(request.json)

            db.session.add(categoria)
            db.session.commit()

            return CategoriaSchema().dump(categoria), 201
        
        except ValidationError as err:
            return err.messages, 422
        except Exception as e:
            return {"message": f"Algo ha salido mal con los categorias {e}"}, 503

    @api.doc(description="Actualiza los datos de una categoria")
    @api.expect(CategoriaSwagger)
    @api.response(200, "Devuelve la categoria actualizada", CategoriaSwagger)
    @api.response(401, "Token invalido")
    @api.response(422, "Error de validacion.") 
    @api.response(404, "Categoria no encontrada.")   
    @api.response(503, "Algo salio mal, intenta de nuevo.")    
    @jwt_required()    
    def put(self):
        try:

            categoria = CategoriaSchemaValidar().load(request.json)
            categoria = CategoriaSchema(transient=True).load(request.json)

            categoriadb = CategoriaModel.query.where(CategoriaModel.IDCATEGORIA == categoria.IDCATEGORIA).one()
            categoriadb.NOMBRE = categoria.NOMBRE

            db.session.commit()

            return CategoriaSchema().dump(categoriadb), 200
        
        except NoResultFound as e:
            return {"msg": f"El categoria indicado no fue encontrado o no existe. {e}"}, 404
        except ValidationError as err:
            return err.messages, 422
        except Exception as e:
            return {"message": f"Algo ha salido mal con los categorias {e}"}, 503
        
class CategoriaControllerById(Resource):
    @api.doc(description="Obtiene una categoria por su ID")
    @api.response(200, "Devuelve la categoria hallada", CategoriaSwagger)
    @api.response(401, "Token invalido")
    @api.response(404, "Categoria no encontrada.")   
    @api.response(503, "Algo salio mal, intenta de nuevo.")
    @jwt_required()
    def get(self, idcategoria):
        try:
            categoriadb = CategoriaModel.query.where(CategoriaModel.IDCATEGORIA == idcategoria).one()

            return CategoriaSchema().dump(categoriadb), 200
        
        except NoResultFound as e:
            return {"msg": f"El categoria indicado no fue encontrado o no existe. {e}"}, 404
        except Exception as e:
            return {"message": f"Algo ha salido mal con los categorias {e}"}, 503

    @jwt_required() 
    @api.doc(description="Elimina una categoria por su ID")
    @api.response(200, "Devuelve un mensaje de confirmacion.")
    @api.response(401, "Token invalido")
    @api.response(404, "Categoria no encontrada.")   
    @api.response(503, "Algo salio mal, intenta de nuevo.")
    def delete(self, idcategoria):
        try:
            categoriadb = CategoriaModel.query.where(CategoriaModel.IDCATEGORIA == idcategoria).one()

            db.session.delete(categoriadb)
            db.session.commit()

            return {"msg": "categoria eliminado correctamente."}, 200
        
        except NoResultFound as e:
            return {"msg": f"El categoria indicado no fue encontrado o no existe. {e}"}, 404
        except Exception as e:
            return {"message": f"Algo ha salido mal con los categorias {e}"}, 503

