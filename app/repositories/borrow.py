from app.models.user import User
from sqlalchemy.orm import Session
from app.models.borrow import Borrow
from fastapi import Depends
from app.core.database import get_db
from app.repositories.base_repo import BaseRepository 


class BorrowRepository(BaseRepository[Borrow]):
    def __init__(self, db: Session):
        self.db = db
        super().__init__(db, Borrow)

    #def get_by_id(self, borrow_id: int) -> Borrow | None:
        # return self.db.query(Borrow).filter(Borrow.id == borrow_id).first()

    #def create(self, borrow: Borrow) -> Borrow:
        # self.db.add(borrow)
        # self.db.commit()
        # self.db.refresh(borrow)
        # return borrow

    #def delete(self, borrow: Borrow) -> None:
        # self.db.delete(borrow)
        # self.db.commit()

    #def update(self, borrow: Borrow) -> Borrow:
        # self.db.commit()
        # self.db.refresh(borrow)
        # return borrow

    def get_active_borrow(self, user_id: int, book_id: int) -> Borrow | None:
        return (
            self.db.query(Borrow)
            .filter(
                Borrow.user_id == user_id,
                Borrow.book_id == book_id,
                Borrow.is_returned == False,
            )
            .first()
        )
