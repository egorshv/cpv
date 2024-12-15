from sqlalchemy.engine import create_engine

from src.backend.dao import DAO
from src.backend.models.cart import Cart
from src.backend.facades.cart import CartFacade
from src.settings import DSN


def get_service(cart):
    engine = create_engine(DSN)
    dao = DAO(engine=engine, model=Cart)
    service = CartFacade(dao=dao, cart=cart)
    return service
