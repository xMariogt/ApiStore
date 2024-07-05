from src.controllers.categoria_controller import CategoriaController, CategoriaControllerById
from flask_restx import Namespace

def CategoriaRoute(api):

    ns_categoria = Namespace("categoria", description="ENDPOINTS de Categorias")

    ns_categoria.add_resource(CategoriaController, "")
    ns_categoria.add_resource(CategoriaControllerById, "/idcategoria/<int:idcategoria>")

    api.add_namespace(ns_categoria)