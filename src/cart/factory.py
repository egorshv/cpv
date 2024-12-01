from sqlalchemy.engine import create_engine

from src.base.dao import DAO
from src.cart.models import Cart
from src.cart.service import CartService
from src.settings import DSN


def get_service(cart):
    engine = create_engine(DSN)
    dao = DAO(engine=engine, model=Cart)
    service = CartService(dao=dao, cart=cart)
    return service
