from sqlalchemy.orm import Mapped, mapped_column

from src.backend.models.base import Base


class Buyer(Base):
    __tablename__ = 'buyer'

    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    delivery_address: Mapped[str]

    def __str__(self):
        return self.first_name
