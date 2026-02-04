from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_borrow_service, get_db
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
    service: BorrowService = Depends(get_borrow_service),
):

    return service.borrow_book(
        user_id=borrow.user_id,
        book_id=borrow.book_id,
        start_date=borrow.start_date,
        return_date=borrow.return_date,
    )


@router.post(
    "/{borrow_id}/return",
    response_model=BorrowResponse,
)
def return_book(
    borrow_id: int,
    service: BorrowService = Depends(get_borrow_service),
):
    return service.return_book(borrow_id)