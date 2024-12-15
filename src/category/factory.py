from sqlalchemy.engine import create_engine

from src.base.dao import DAO
from src.category.models import MedicineCategory
from src.category.facade import MedicineCategoryFacade
from src.settings import DSN


def get_service(category):
    engine = create_engine(DSN)
    dao = DAO(engine=engine, model=MedicineCategory)
    service = MedicineCategoryFacade(dao, category)
    return service
