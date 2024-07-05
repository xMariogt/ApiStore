import datetime
from src.common.utils import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey

class PedidoModel(db.Model):
    __tablename__ = "PEDIDO"

    IDPEDIDO: Mapped[int] = mapped_column(primary_key=True)
    FECHA_PEDIDO: Mapped[datetime.datetime] = mapped_column(nullable=False)
    TOTAL: Mapped[float] = mapped_column(nullable=False)
    CANTIDAD: Mapped[float] = mapped_column(nullable=False)
    IDUSUARIO: Mapped[int] = mapped_column(Integer, ForeignKey("USUARIO.IDUSUARIO"), nullable=False)
    IDPRODUCTO: Mapped[int] = mapped_column(Integer, ForeignKey("PRODUCTO.IDPRODUCTO"), nullable=False)
    IDMETODO: Mapped[int] = mapped_column(Integer, ForeignKey("METODO_PAGO.IDMETODO"), nullable=False)

    #Relationships
    USUARIO: Mapped["UsuarioModel"] = relationship()