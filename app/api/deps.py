from app.core.database import _db, get_db
from app.repositories.book import BookRepository
from app.services.book import BookService
from sqlalchemy.orm import Session
from typing import Generator
from app.repositories.book import BookRepository

# def get_db_session(db:Session = Depends(get_db))->Session:
#     return db

# def get_book_repo(db: Session = Depends(get_db_session)):
#     return BookRepository(db=db)

# def get_book_service():
#     return BookService(book_repo=get_book_repo())