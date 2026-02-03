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
