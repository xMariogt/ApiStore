from src.controllers.pedido_controller import PedidoController, PedidoControllerById, PedidoControllerByUser
from src.common.utils import api
from flask_restx import Namespace

def PedidoRoute(api):

    ns_pedido = Namespace("pedido", description="ENDPOINTS de pedidos")

    ns_pedido.add_resource(PedidoController, "")
    ns_pedido.add_resource(PedidoControllerByUser, "/idusuario/<int:idusuario>")
    ns_pedido.add_resource(PedidoControllerById, "/idpedido/<int:idpedido>")

    api.add_namespace(ns_pedido)