from sqlalchemy.engine import create_engine

from src.base.dao import DAO
from src.cart.models import Cart
from src.cart.facade import CartFacade
from src.settings import DSN


def get_service(cart):
    engine = create_engine(DSN)
    dao = DAO(engine=engine, model=Cart)
    service = CartFacade(dao=dao, cart=cart)
    return service
