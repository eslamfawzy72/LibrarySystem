from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.book import BookCreate, BookResponse
from app.services.book import BookService

router = APIRouter(prefix="/books", tags=["Books"])


@router.post(
    "",
    response_model=BookResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_book(
    book: BookCreate,
    db: Session = Depends(get_db),
):
    book_service = BookService()
    return book_service.create_book(
        db,
        title=book.title,
        author=book.author,
        total_copies=book.total_copies,
    )

@router.get(
    "/{book_id}",
    response_model=BookResponse,
    status_code=status.HTTP_200_OK,
)
def get_book(
    book_id: int,
    db: Session = Depends(get_db),
):
    book_service = BookService()
    book = book_service.get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
@router.get(
    "",
    response_model=list[BookResponse],
    status_code=status.HTTP_200_OK,
)
def get_books(
    db: Session = Depends(get_db),
):
    book_service = BookService()
    return book_service.get_books(db)
@router.get(
    "/title/{title}",
    response_model=BookResponse,
    status_code=status.HTTP_200_OK,
)
def get_book_by_title(
    title: str,
    db: Session = Depends(get_db),
):
    book = book_service.get_book_by_title(db, title)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
