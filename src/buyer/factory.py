from sqlalchemy.engine import create_engine

from src.base.dao import DAO
from src.buyer.models import Buyer
from src.buyer.facade import BuyerFacade
from src.settings import DSN


def get_service(buyer):
    engine = create_engine(DSN)
    dao = DAO(model=Buyer, engine=engine)
    service = BuyerFacade(dao=dao, buyer=buyer)
    return service