from src.base.dao import DAO
from src.base.facade import BaseFacade


class BuyerFacade(BaseFacade):
    def __init__(self, buyer, dao: DAO):
        self.buyer = buyer
        super().__init__(dao)

    def update_address(self, new_address):
        self.dao.update(self.buyer.id, delivery_address=new_address)

    def update_email(self, new_email):
        self.dao.update(self.buyer.id, email=new_email)
