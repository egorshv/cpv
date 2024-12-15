from sqlalchemy import select, update
from sqlalchemy.orm import Session


class DAO:
    def __init__(self, model, engine):
        self.engine = engine
        self.model = model

    def create(self, object_to_create):
        session = Session(self.engine)
        session.add(object_to_create)
        session.commit()
        session.close()

    def update(self, object_id: int, **kwargs):
        session = Session(self.engine)
        session.execute(update(self.model).where(self.model.id == object_id).values(**kwargs))
        session.commit()
        session.close()

    def get(self, **kwargs):
        session = Session(self.engine)
        obj = session.scalars(select(self.model).filter_by(**kwargs)).first()
        session.close()
        return obj

    def list(self, **kwargs):
        session = Session(self.engine)
        obj = session.scalars(select(self.model).filter_by(**kwargs)).all()
        session.close()
        return obj

    def get_all(self):
        session = Session(self.engine)
        objects = session.scalars(select(self.model)).all()
        session.close()
        return objects

    def delete(self, object_id: int):
        session = Session(self.engine)
        object_to_delete = session.scalars(select(self.model).where(self.model.id == object_id)).first()
        session.delete(object_to_delete)
        session.commit()
        session.close()
