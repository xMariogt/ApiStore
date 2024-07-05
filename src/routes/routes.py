from .metodo_route import MetodoRoute
from .categoria_route import CategoriaRoute
from .producto_route import ProductoRoute
from .usuario_route import UsuarioRoute
from .pedido_route import PedidoRoute

def Routes(api):
    UsuarioRoute(api)
    ProductoRoute(api)
    CategoriaRoute(api)
    MetodoRoute(api)
    PedidoRoute(api)