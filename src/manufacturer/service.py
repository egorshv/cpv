from src.base.service import BaseService


class ManufacturerService(BaseService):
    def __init__(self, manufacturer, dao):
        self.manufacturer = manufacturer
        super().__init__(dao)

    def add_medicine(self, medicine):
        if not medicine.manufacturer:
            return self.dao.update(medicine.id, manufacturer=self.manufacturer)
        raise ValueError()

    def remove_medicine(self, medicine):
        if medicine.manufacturer and medicine.manufacturer == self.manufacturer:
            return self.dao.update(medicine.id, manufacturer=None)
        raise ValueError()

    def get_medicines(self):
        return self.manufacturer.medicines
