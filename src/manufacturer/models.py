from sqlalchemy.orm import Mapped, relationship

from src.base.models import Base


class Manufacturer(Base):
    __tablename__ = 'manufacturer'

    name: Mapped[str]
    country_foreign: Mapped[str]
    medicines: Mapped[list['Medicine']] = relationship(back_populates='manufacturer')
