from src.base.dao import DAO
from src.base.service import BaseService
from src.cart.models import Cart


class CartService(BaseService):
    def __init__(self, cart: Cart, dao: DAO):
        self.cart = cart
        super().__init__(dao)

    def add_medicine(self, medicine, quantity):
        if new_quantity := medicine.stock_quantity - quantity >= 0:
            return self.dao.update(medicine.id, cart=self.cart, stock_quantity=new_quantity)
        raise ValueError()

    def remove_medicine(self, medicine):
        if medicine.cart == self.cart:
            return self.dao.update(medicine.id, cart=None, stock_quantity=medicine.stock_quantity + 1)
        raise ValueError()

    def get_total_price(self):
        total_price = 0
        for medicine in self.cart.medicines:
            total_price += medicine.price
        return total_price

    def get_medicines(self):
        return self.cart.medicines
