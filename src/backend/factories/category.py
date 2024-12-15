from sqlalchemy.engine import create_engine

from src.backend.dao import DAO
from src.backend.models.category import MedicineCategory
from src.backend.facades.category import MedicineCategoryFacade
from src.settings import DSN


def get_service(category):
    engine = create_engine(DSN)
    dao = DAO(engine=engine, model=MedicineCategory)
    service = MedicineCategoryFacade(dao, category)
    return service
