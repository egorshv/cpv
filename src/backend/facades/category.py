from src.backend.dao import DAO
from src.backend.facades.base import BaseFacade


class MedicineCategoryFacade(BaseFacade):
    def __init__(self, dao: DAO, category):
        self.category = category
        super().__init__(dao)

    def add_medicine(self, medicine):
        if not medicine.category:
            return self.dao.update(medicine.id, category=self.category)
        raise ValueError()

    def remove_medicine(self, medicine):
        if medicine.category and medicine.category == self.category:
            return self.dao.update(medicine.id, category=None)
        raise ValueError()

    def get_medicines(self):
        medicines = self.dao.get(category=self.category)
        return medicines
