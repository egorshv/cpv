import abc


class BaseDAO(abc.ABC):
    def __init__(self, model):
        self.model = model

    @abc.abstractmethod
    def create(self, data: dict):
        raise NotImplementedError()

    @abc.abstractmethod
    def get_all(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, object_id: int):
        raise NotImplementedError()
