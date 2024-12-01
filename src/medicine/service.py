from src.base.service import BaseService


class MedicineService(BaseService):
    def __init__(self, medicine, dao):
        self.medicine = medicine
        super().__init__(dao)

    def get_details(self):
        return self.medicine

    def update_stock(self, stock):
        self.dao.update(self.medicine.id, stock_quantity=stock)

    def update_price(self, price):
        self.dao.update(self.medicine.id, price=price)
