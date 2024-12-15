from src.backend.dao import DAO
from src.backend.facades.base import BaseFacade
from src.backend.models.cart import Cart
from src.backend.models.medicine import Medicine


class CartFacade(BaseFacade):
    def __init__(self, cart: Cart, dao: DAO):
        self.cart = cart
        self.medicine_dao = DAO(
            engine=dao.engine,
            model=Medicine,
        )
        super().__init__(dao)

    def add_medicine(self, medicine, quantity = 1):
        if (new_quantity := medicine.stock_quantity - quantity) >= 0:
            return self.medicine_dao.update(medicine.id, cart_id=self.cart.id)
        raise ValueError()

    def remove_medicine(self, medicine):
        return self.medicine_dao.update(medicine.id, cart_id=None)

    def get_total_price(self):
        total_price = 0
        medicines = self.medicine_dao.list(cart_id=self.cart.id)
        for medicine in medicines:
            total_price += medicine.price
        return total_price

    def get_medicines(self):
        return self.cart.medicines
