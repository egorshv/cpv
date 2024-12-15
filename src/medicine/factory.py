from sqlalchemy.engine import create_engine

from src.base.dao import DAO
from src.medicine.models import Medicine
from src.medicine.facade import MedicineFacade
from src.settings import DSN


def get_service(medicine):
    engine = create_engine(DSN)
    dao = DAO(engine=engine, model=Medicine)
    service = MedicineFacade(dao=dao, medicine=medicine)
    return service
