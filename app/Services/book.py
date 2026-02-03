from sqlalchemy.orm import Session
from app.models.book import Book
from app.repositories.book import BookRepository


class BookService:
    def __init__(self):
        self.book_repo = BookRepository()

    def create_book(
        self,
        db: Session,
        title: str,
        author: str,
        total_copies: int,
    ) -> Book:
        book = Book(
            title=title,
            author=author,
            total_copies=total_copies,
            available_copies=total_copies,
        )
        return self.book_repo.create(db, book)
    def get_book_by_id(self, db: Session, book_id: int) -> Book | None:
        return self.book_repo.get_by_id(db, book_id)
    def get_books(self, db: Session) -> list[Book]:
        return self.book_repo.list_all(db)
    def get_book_by_title(self, db: Session, title: str) -> Book | None:
        return db.query(Book).filter(Book.title == title).first()
