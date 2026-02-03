from sqlalchemy.orm import Session
from app.models.book import Book


class BookRepository:

    def get_by_id(self, db: Session, book_id: int) -> Book | None:
        return db.query(Book).filter(Book.id == book_id).first()

    def list_all(self, db: Session) -> list[Book]:
        return db.query(Book).all()

    def create(self, db: Session, book: Book) -> Book:
        db.add(book)
        db.commit()
        db.refresh(book)
        return book

    def delete(self, db: Session, book: Book) -> None:
        db.delete(book)
        db.commit()

    def update(self, db: Session, book: Book) -> Book:
        db.commit()
        db.refresh(book)
        return book
