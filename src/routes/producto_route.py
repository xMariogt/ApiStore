from flask_restx import Namespace

from src.controllers.producto_controller import ProductoController, ProductoControllerById

def ProductoRoute(api):

    ns_producto = Namespace("producto", description="ENDPOINTS de los productos")

    ns_producto.add_resource(ProductoController, "")
    ns_producto.add_resource(ProductoControllerById, "/idproducto/<int:idproducto>")

    api.add_namespace(ns_producto)