from sqlalchemy.orm import Mapped, relationship

import src.backend.models.base


class MedicineCategory(src.backend.models.base.Base):
    __tablename__ = 'medicine_category'

    name: Mapped[str]
    description: Mapped[str]
    medicines: Mapped[list['Medicine']] = relationship(back_populates='category')

    def __str__(self):
        return self.name
