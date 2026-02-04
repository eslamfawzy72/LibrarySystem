from app.core.database import _db, get_db
from app.repositories.book import BookRepository
from app.repositories.borrow import BorrowRepository
from app.services.book import BookService
from app.services.borrow import BorrowService
from app.services.user import UserService
from sqlalchemy.orm import Session
from typing import Generator
from app.repositories.book import BookRepository
from app.repositories.user import UserRepository

from fastapi import Depends


def get_db_session(db: Session = Depends(get_db)) -> Session:
    return db


def get_borrow_repo(db: Session = Depends(get_db_session)) -> BorrowRepository:
    return BorrowRepository(db=db)


def get_book_repo(db: Session = Depends(get_db_session)) -> BookRepository:
    return BookRepository(db=db)


def get_user_repo(db: Session = Depends(get_db_session)) -> UserRepository:
    return UserRepository(db=db)


def get_book_service(
    book_repo: BookRepository = Depends(get_book_repo),
):
    return BookService(book_repo=book_repo)


def get_borrow_service(
    borrow_repo: BorrowRepository = Depends(get_borrow_repo),
    book_repo: BookRepository = Depends(get_book_repo),
) -> BorrowService:
    return BorrowService(
        borrow_repo=borrow_repo,
        book_repo=book_repo,
    )


def get_user_service(
    user_repo: "UserRepository" = Depends(get_user_repo),
) -> "UserService":
    return UserService(user_repo=user_repo)
