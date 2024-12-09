from src.base.dao import DAO
from src.base.service import BaseService
from src.cart.models import Cart
from src.medicine.models import Medicine


class CartService(BaseService):
    def __init__(self, cart: Cart, dao: DAO):
        self.cart = cart
        self.medicine_dao = DAO(
            engine=dao.engine,
            model=Medicine,
        )
        super().__init__(dao)

    def add_medicine(self, medicine, quantity = 1):
        if (new_quantity := medicine.stock_quantity - quantity) >= 0:
            return self.medicine_dao.update(medicine.id, cart_id=self.cart.id, stock_quantity=new_quantity)
        raise ValueError()

    def remove_medicine(self, medicine):
        return self.medicine_dao.update(medicine.id, cart_id=None, stock_quantity=medicine.stock_quantity + 1)

    def get_total_price(self):
        total_price = 0
        for medicine in self.cart.medicines:
            total_price += medicine.price
        return total_price

    def get_medicines(self):
        return self.cart.medicines
