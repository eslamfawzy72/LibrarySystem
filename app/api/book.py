from app.api.deps import get_book_service
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

# from app.api.deps import get_book_service, get_db
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
    service: BookService = Depends(get_book_service),
):
    return service.create_book(
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
    service: BookService = Depends(get_book_service),
):

    book = service.get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.get(
    "",
    response_model=list[BookResponse],
    status_code=status.HTTP_200_OK,
)
def get_books(
    service: BookService = Depends(get_book_service),
):
    return service.get_books()


@router.get(
    "/title/{title}",
    response_model=BookResponse,
    status_code=status.HTTP_200_OK,
)
def get_book_by_title(
    title: str,
    service: BookService = Depends(get_book_service),
):
    book = service.get_book_by_title(title)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
