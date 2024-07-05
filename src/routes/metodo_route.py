from flask_restx import Namespace

from src.controllers.metodo_controller import MetodoController, MetodoControllerById

def MetodoRoute(api):

    ns_metodo = Namespace("metodo", description="ENDPOINTS para Metodos de Pago")

    ns_metodo.add_resource(MetodoController, "")
    ns_metodo.add_resource(MetodoControllerById, "/idmetodo/<int:idmetodo>")

    api.add_namespace(ns_metodo)