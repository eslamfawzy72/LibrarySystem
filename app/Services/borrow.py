from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.models.borrow import Borrow
from app.repositories.borrow import BorrowRepository
from app.repositories.book import BookRepository


class BorrowService:
    def __init__(self):
        self.borrow_repo = BorrowRepository()
        self.book_repo = BookRepository()

    from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.models.borrow import Borrow
from app.repositories.borrow import BorrowRepository
from app.repositories.book import BookRepository


class BorrowService:
    MAX_BORROW_DAYS = 14  # business rule

    def __init__(self):
        self.borrow_repo = BorrowRepository()
        self.book_repo = BookRepository()

    def borrow_book(
        self,
        db: Session,
        user_id: int,
        book_id: int,
        start_date: datetime,
        return_date: datetime,
    ) -> Borrow:

        now = datetime.utcnow()

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
        book = self.book_repo.get_by_id(db, book_id)
        if not book:
            raise ValueError("Book not found")

        #  Check availability
        if book.available_copies <= 0:
            raise ValueError("Book not available")

        #  Check if user already borrowed this book
        active = self.borrow_repo.get_active_borrow(db, user_id, book_id)
        if active:
            raise ValueError("User already borrowed this book")

        #  Create borrow
        borrow = Borrow(
            user_id=user_id,
            book_id=book_id,
            start_date=start_date,
            return_date=return_date,
        )

        # 6️⃣ Update availability
        book.available_copies -= 1

        self.borrow_repo.create(db, borrow)
        self.book_repo.update(db, book)

        return borrow


def return_book(
        self,
        db: Session,
        borrow_id: int,
    ) -> Borrow:

        # Fetch borrow record
        borrow = self.borrow_repo.get_by_id(db, borrow_id)
        if not borrow:
            raise ValueError("Borrow record not found")

        # Prevent double return
        if borrow.return_date is not None:
            raise ValueError("Book already returned")

        #  Set actual return time
        now = datetime.utcnow()
        borrow.return_date = now

        #  Update book availability
        book = borrow.book
        book.available_copies += 1

        #  Persist changes
        self.borrow_repo.update(db, borrow)
        self.book_repo.update(db, book)

        return borrow
