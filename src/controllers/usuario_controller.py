import datetime
from flask_restx import Resource
from src.common.utils import db, api
from marshmallow import ValidationError
from src.models.usuario_model import UsuarioModel
from src.schemas.usuario_schema import UsuarioSchema, UsuarioSchemaLogin, UsuarioSchemaValidar
from src.swagger.usuario_swagger import UsuarioSwagger, UsuarioSwaggerPost, LoginSwagger
from sqlalchemy.exc import NoResultFound
from flask_jwt_extended import create_access_token, jwt_required
from flask import request

class UsuarioController(Resource):
    @api.doc(description="Obtiene todos los usuarios")
    @api.response(200, "Devuelve un array de usuarios", UsuarioSwagger, as_list=True)
    @api.response(401, "Token invalido")
    @api.response(503, "Algo salio mal, intenta de nuevo.")
    @jwt_required()     
    def get(self):
        try:
            usuariosdb = UsuarioModel.query.all()

            usuarios = UsuarioSchema(many=True)
    
            return usuarios.dump(usuariosdb), 200
        
        except Exception as e:
            return {"message": f"Algo ha salido mal con los usuarios {e}"}, 503

    @api.doc(description="Agrega un usuario")
    @api.expect(UsuarioSwaggerPost)
    @api.response(200, "Devuelve el usuario insertado", UsuarioSwagger)
    @api.response(401, "Token invalido")
    @api.response(422, "Error de validacion")    
    @api.response(503, "Algo salio mal, intenta de nuevo.")
    @jwt_required()     
    def post(self):
        try:

            usuariodb = UsuarioSchemaValidar(exclude=["IDUSUARIO"]).load(request.json)
            usuariodb = UsuarioSchema(transient=True).load(request.json)

            db.session.add(usuariodb)
            db.session.commit()

            return UsuarioSchema().dump(usuariodb), 201
        
        except ValidationError as err:
            return err.messages, 422
        except Exception as e:
            return {"message": f"Algo ha salido mal con los usuarios {e}"}

    @api.doc(description="Actualiza los datos de un usuario")
    @api.expect(UsuarioSwagger)
    @api.response(200, "Devuelve el usuario actualizado.", UsuarioSwagger)
    @api.response(401, "Token invalido")
    @api.response(422, "Error de validacion.") 
    @api.response(404, "Usuario no encontrado.")   
    @api.response(503, "Algo salio mal, intenta de nuevo.")
    @jwt_required() 
    def put(self):
        try:

            usuariodata = UsuarioSchemaValidar().load(request.json)
            usuariodata = UsuarioSchema(transient=True).load(request.json)

            usuariodb = UsuarioModel.query.where(UsuarioModel.IDUSUARIO == usuariodata.IDUSUARIO).one()

            usuariodb.NOMBRE = usuariodata.NOMBRE
            usuariodb.APELLIDO = usuariodata.APELLIDO

            db.session.commit()

            return UsuarioSchema().dump(usuariodb), 200
        
        except NoResultFound as e:
            return {"message": "No se encontro el usuario."}, 404
        except ValidationError as err:
            return err.messages, 422
        except Exception as e:
            return {"message": f"Algo ha salido mal con los usuarios {e}"}
        
class UsuarioControllerById(Resource):
    @api.doc(description="Elimina a un usuario")
    @api.response(200, "Devuelve un mensaje de confirmacion.")
    @api.response(401, "Token invalido")
    @api.response(404, "Usuario no encontrado.")   
    @api.response(503, "Algo salio mal, intenta de nuevo.")
    @jwt_required() 
    def delete(self, idusuario):
        try:
            usuario = UsuarioModel.query.where(UsuarioModel.IDUSUARIO == idusuario).one()

            db.session.delete(usuario)
            db.session.commit()

            return {"message": "Usuario eliminado con exito."}, 200
        
        except NoResultFound as e:
            return {"message": "No se encontro el usuario."}, 404
        except Exception as e:
            return {"message": f"Algo ha salido mal al eliminar al usuario. {e}"}, 503
    
    @api.doc(description="Obtiene un usuario por su ID")
    @api.response(200, "Devuelve el usuario indicado.", UsuarioSwagger)
    @api.response(401, "Token invalido")
    @api.response(404, "Usuario no encontrado.")   
    @api.response(503, "Algo salio mal, intenta de nuevo.")
    @jwt_required() 
    def get(self, idusuario):
        try:
            usuariodb = UsuarioModel.query.where(UsuarioModel.IDUSUARIO == idusuario).one()

            return UsuarioSchema().dump(usuariodb), 200
        
        except NoResultFound as e:
            return {"message": "No se encontro el usuario."}, 404
        except Exception as e:
            return {"message": f"Algo ha salido mal con los usuarios {e}"}, 503
        
class Login(Resource):
    @api.doc(description="Agrega un usuario")
    @api.expect(LoginSwagger)
    @api.response(200, "Devuelve el token")
    @api.response(422, "Error de validacion")    
    @api.response(404, "Correo o password no coinciden.")  
    @api.response(503, "Algo salio mal, intenta de nuevo.")
    def post(self):
        try:

            usuario = UsuarioSchemaLogin().load(request.json)
            usuariodb = UsuarioModel.query.where(UsuarioModel.CORREO == usuario["CORREO"]).where(
                UsuarioModel.PASSWORD == usuario["PASSWORD"]).one()
            
            usuario_schema = UsuarioSchema(exclude=["PASSWORD",]).dump(usuariodb)
            access_token = create_access_token(identity=usuario_schema, expires_delta=datetime.timedelta(days=1))

            return {"token": access_token}, 200
        
        except NoResultFound as e:
            return {"message": "Correo o contrania equivocados."}, 404
        except ValidationError as err:
            return err.messages, 422
        except Exception as e:
            return {"message": f"Algo ha salido mal con los usuarios {e}"}, 503
