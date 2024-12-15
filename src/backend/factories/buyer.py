from sqlalchemy.engine import create_engine

from src.backend.dao import DAO
from src.backend.models.buyer import Buyer
from src.backend.facades.buyer import BuyerFacade
from src.settings import DSN


def get_service(buyer):
    engine = create_engine(DSN)
    dao = DAO(model=Buyer, engine=engine)
    service = BuyerFacade(dao=dao, buyer=buyer)
    return service