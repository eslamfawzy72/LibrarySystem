from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session
from app.models.borrow import Borrow
from app.repositories.borrow import BorrowRepository
from app.repositories.book import BookRepository
from fastapi import Depends


class BorrowService:     
    MAX_BORROW_DAYS = 14  # business rule
    def __init__ (self,borrow_repo: BorrowRepository, book_repo: BookRepository):
        self.borrow_repo = borrow_repo
        self.book_repo = book_repo

    # def __init__(self):
    #     self.borrow_repo = BorrowRepository()
    #     self.book_repo = BookRepository()

    def borrow_book(
        self,
        user_id: int,
        book_id: int,
        start_date: datetime,
        return_date: datetime,
    ) -> Borrow:

        now = datetime.now(timezone.utc)

        # Date validation
        if start_date >= return_date:
            raise ValueError("start_date must be before return_date")

        if start_date < now:
            raise ValueError("start_date cannot be in the past")

        max_return_date = start_date + timedelta(days=self.MAX_BORROW_DAYS)
        if return_date > max_return_date:
            raise ValueError(
                f"Borrow duration cannot exceed {self.MAX_BORROW_DAYS} days"
            )

        #  Check book exists
        book = self.book_repo.get_by_id(book_id)
        if not book:
            raise ValueError("Book not found")

        #  Check availability
        if book.available_copies <= 0:
            raise ValueError("Book not available")

        #  Check if user already borrowed this book
        active = self.borrow_repo.get_active_borrow(user_id, book_id)
        if active:
            raise ValueError("User already borrowed this book")

        #  Create borrow
        borrow = Borrow(
            user_id=user_id,
            book_id=book_id,
            start_date=start_date,
            return_date=return_date,
            is_returned=False
        )

        # Update availability
        book.available_copies -= 1

        self.borrow_repo.create(borrow)
        self.book_repo.update(book)

        return borrow

    def return_book(
        self,
        borrow_id: int,
    ) -> Borrow:

        # Fetch borrow record
        borrow = self.borrow_repo.get_by_id(borrow_id)
        if not borrow:
            raise ValueError("Borrow record not found")

        # Prevent double return
        if borrow.is_returned:
            raise ValueError("Book already returned")

        # Set return time
        now = datetime.now(timezone.utc)
        borrow.return_date = now
        borrow.is_returned = True

        #  Update book availability
        book = borrow.book
        book.available_copies += 1

        #  Persist changes
        self.borrow_repo.update(borrow)
        self.book_repo.update(book)

        return borrow
