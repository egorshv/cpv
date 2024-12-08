from sqlalchemy.orm import Mapped, relationship

from src.base.models import Base


class MedicineCategory(Base):
    __tablename__ = 'medicine_category'

    name: Mapped[str]
    description: Mapped[str]
    medicines: Mapped[list['Medicine']] = relationship(back_populates='category')

    def __str__(self):
        return self.name
