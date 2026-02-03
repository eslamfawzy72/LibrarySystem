from sqlalchemy.orm import Session
from app.models.borrow import Borrow


class BorrowRepository:

    def get_by_id(self, db: Session, borrow_id: int) -> Borrow | None:
        return db.query(Borrow).filter(Borrow.id == borrow_id).first()

    def create(self, db: Session, borrow: Borrow) -> Borrow:
        db.add(borrow)
        db.commit()
        db.refresh(borrow)
        return borrow

    def delete(self, db: Session, borrow: Borrow) -> None:
        db.delete(borrow)
        db.commit()

    def update(self, db: Session, borrow: Borrow) -> Borrow:
        db.commit()
        db.refresh(borrow)
        return borrow

    def get_active_borrow(
        self, db: Session, user_id: int, book_id: int
    ) -> Borrow | None:
        return (
            db.query(Borrow)
            .filter(
                Borrow.user_id == user_id,
                Borrow.book_id == book_id,
                Borrow.return_date.is_(None),
            )
            .first()
        )
