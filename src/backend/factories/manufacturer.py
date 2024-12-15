from sqlalchemy.engine import create_engine

from src.backend.dao import DAO
from src.backend.models.manufacturer import Manufacturer
import src.backend.facades.manufacturer
from src.settings import DSN


def get_service(manufacturer):
    engine = create_engine(DSN)
    dao = DAO(engine=engine, model=Manufacturer)
    service = src.backend.facades.manufacturer.ManufacturerFacade(manufacturer=manufacturer, dao=dao)
    return service
