from src.controllers.usuario_controller import Login, UsuarioController, UsuarioControllerById
from flask_restx import Namespace
def UsuarioRoute(api):

    ns_usuario = Namespace('usuario', description='ENDPOINTS de Usuarios')

    ns_usuario.add_resource(UsuarioController, "")
    ns_usuario.add_resource(UsuarioControllerById, "/idusuario/<int:idusuario>")
    ns_usuario.add_resource(Login, "/login")

    api.add_namespace(ns_usuario)