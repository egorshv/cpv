from src.base.dao import DAO


class BaseFacade:
    def __init__(self, dao: DAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def delete(self, object_id: int):
        return self.dao.delete(object_id)