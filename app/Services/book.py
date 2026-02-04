from sqlalchemy.orm import Session
from app.models.book import Book
from app.repositories.book import BookRepository
from fastapi import Depends


class BookService:
    def __init__(self, book_repo: BookRepository):
        self.book_repo = book_repo

    def create_book(
        self,
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
        return self.book_repo.create(book)
    
    def get_book_by_id(self, book_id: int) -> Book | None:
        return self.book_repo.get_by_id(book_id)
    
    def get_books(self) -> list[Book]:
        return self.book_repo.list_all()
    
    def get_book_by_title(self, title: str) -> Book | None:
        return self.book_repo.get_by_title(title)