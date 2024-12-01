import abc

from src.base.dao import BaseDAO


class BaseService(abc.ABC):
    def __init__(self, dao: BaseDAO):
        self.dao = dao

    @abc.abstractmethod
    def get_details(self):
        raise NotImplementedError()

    def get_all(self):
        return self.dao.get_all()

    def delete(self, object_id: int):
        return self.dao.delete(object_id)