from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from src.base.models import Base
from src.category.models import MedicineCategory
from src.manufacturer.models import Manufacturer
from src.cart.models import Cart


class Medicine(Base):
    __tablename__ = 'medicine'

    name: Mapped[str]
    price: Mapped[float]
    description: Mapped[str]
    stock_quantity: Mapped[int]

    cart_id: Mapped[int] = mapped_column(ForeignKey('cart.id'), nullable=True)
    cart: Mapped['Cart'] = relationship(back_populates='medicines', lazy='subquery')

    category_id: Mapped[int] = mapped_column(ForeignKey('medicine_category.id'), nullable=True)
    category: Mapped['MedicineCategory'] = relationship(back_populates='medicines', lazy='subquery')

    manufacturer_id: Mapped[int] = mapped_column(ForeignKey('manufacturer.id'), nullable=True)
    manufacturer: Mapped['Manufacturer'] = relationship(back_populates='medicines', lazy='subquery')
