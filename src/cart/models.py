from sqlalchemy.orm import Mapped, relationship

from src.base.models import Base


class Cart(Base):
    __tablename__ = 'cart'

    medicines: Mapped[list['Medicine']] = relationship(back_populates='cart')
