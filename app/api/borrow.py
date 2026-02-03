from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.borrow import BorrowCreate, BorrowResponse
from app.services.borrow import BorrowService

router = APIRouter(prefix="/borrows", tags=["Borrows"])


@router.post(
    "",
    response_model=BorrowResponse,
    status_code=status.HTTP_201_CREATED,
)
def borrow_book(
    borrow: BorrowCreate,
    db: Session = Depends(get_db),
):
    try:
        borrow_service = BorrowService()
        return borrow_service.borrow_book(
            db,
            user_id=borrow.user_id,
            book_id=borrow.book_id,
            start_date=borrow.start_date,
            return_date=borrow.return_date,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post(
    "/{borrow_id}/return",
    response_model=BorrowResponse,
)
def return_book(
    borrow_id: int,
    db: Session = Depends(get_db),
):
    try:
        borrow_service = BorrowService()
        return borrow_service.return_book(db, borrow_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
