from src.common.utils import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, ForeignKey


class ProductoModel(db.Model):
    __tablename__ = "PRODUCTO"

    IDPRODUCTO: Mapped[int] = mapped_column(primary_key=True)
    NOMBRE: Mapped[str] = mapped_column(nullable=False)
    DESCRIPCION: Mapped[str] = mapped_column(nullable=False)
    PRECIO: Mapped[float] = mapped_column(nullable=False)
    STOCK: Mapped[int] = mapped_column(nullable=False)
    IDCATEGORIA: Mapped[int] = mapped_column(Integer, ForeignKey("CATEGORIA.IDCATEGORIA"), nullable=False)
    