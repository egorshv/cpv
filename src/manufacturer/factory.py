from sqlalchemy.engine import create_engine

from src.base.dao import DAO
from src.manufacturer.models import Manufacturer
from src.manufacturer.facade import ManufacturerFacade
from src.settings import DSN


def get_service(manufacturer):
    engine = create_engine(DSN)
    dao = DAO(engine=engine, model=Manufacturer)
    service = ManufacturerFacade(manufacturer=manufacturer, dao=dao)
    return service
