from typing import Generic, TypeVar, Type
from sqlalchemy.orm import Session

ModelType = TypeVar("ModelType")

class BaseRepository(Generic[ModelType]):
    def __init__(self, db: Session, model: Type[ModelType]):
        self.db = db
        self.model = model

    def create(self, obj: ModelType):
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get_by_id(self, id: int):
        return self.db.query(self.model).filter(self.model.id == id).first()

    def get_all(self):
        return self.db.query(self.model).all()
    
    def update(self, obj: ModelType):
        self.db.commit()
        self.db.refresh(obj)
        return obj
