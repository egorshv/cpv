from sqlalchemy.engine import create_engine

from src.backend.dao import DAO
from src.backend.models.medicine import Medicine
from src.backend.facades.medicine import MedicineFacade
from src.settings import DSN


def get_service(medicine):
    engine = create_engine(DSN)
    dao = DAO(engine=engine, model=Medicine)
    service = MedicineFacade(dao=dao, medicine=medicine)
    return service
