from sqlalchemy.orm import Mapped

from src.base.models import Base


class Buyer(Base):
    __tablename__ = 'buyer'

    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str]
    delivery_address: Mapped[str]
