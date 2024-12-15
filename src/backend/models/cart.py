from sqlalchemy.orm import Mapped, relationship

from src.backend.models.base import Base


class Cart(Base):
    __tablename__ = 'cart'

    medicines: Mapped[list['Medicine']] = relationship(back_populates='cart', lazy='subquery')

    def __str__(self):
        return f'Cart {self.id}'
