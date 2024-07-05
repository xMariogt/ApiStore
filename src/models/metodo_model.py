from src.common.utils import db
from sqlalchemy.orm import Mapped, mapped_column

class MetodoModel(db.Model):
    __tablename__ = "METODO_PAGO"
    
    IDMETODO: Mapped[int] = mapped_column(primary_key=True)
    NOMBRE: Mapped[str] = mapped_column(nullable=False)