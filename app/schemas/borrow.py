from pydantic import BaseModel, Field
from datetime import datetime

class BorrowCreate(BaseModel):
    user_id: int = Field(..., gt=0)
    book_id: int = Field(..., gt=0)
    start_date: datetime
    return_date: datetime


class BorrowResponse(BaseModel):
    id: int = Field(..., description="Borrow record ID")
    user_id: int = Field(..., description="ID of the user who borrowed the book")
    book_id: int = Field(..., description="ID of the borrowed book")
    is_returned: bool = Field(..., description="Whether the book has been returned")
    start_date: datetime = Field(..., description="Borrow start date")
    return_date: datetime | None = Field(
        None,
        description="Return date (null if not returned yet)"
    )

    class Config:
        from_attributes = True