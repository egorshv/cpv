from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from src.backend.models.base import Base
from src.backend.models.category import MedicineCategory
from src.backend.models.manufacturer import Manufacturer
from src.backend.models.cart import Cart


class Medicine(Base):
    __tablename__ = 'medicine'

    name: Mapped[str] = mapped_column(unique=True)
    price: Mapped[float]
    description: Mapped[str]
    stock_quantity: Mapped[int]

    cart_id: Mapped[int] = mapped_column(ForeignKey('cart.id'), nullable=True)
    cart: Mapped['Cart'] = relationship(back_populates='medicines', lazy='subquery')

    category_id: Mapped[int] = mapped_column(ForeignKey('medicine_category.id'), nullable=True)
    category: Mapped['MedicineCategory'] = relationship(back_populates='medicines', lazy='subquery')

    manufacturer_id: Mapped[int] = mapped_column(ForeignKey('manufacturer.id'), nullable=True)
    manufacturer: Mapped['Manufacturer'] = relationship(back_populates='medicines', lazy='subquery')

    def __str__(self):
        return self.name
