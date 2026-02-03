from pydantic import BaseModel, Field
from datetime import datetime

class BookBase(BaseModel):
    title: str = Field(
        ...,
        min_length=1,
        max_length=100
    )
    author: str = Field(
        ...,
        min_length=3,
        max_length=100
    )

class BookCreate(BookBase):
    total_copies: int = Field(
        ...,
        ge=1,
        description="Total number of book copies"
    )

class BookResponse(BookBase):
    id: int
    total_copies: int
    available_copies: int
    created_at: datetime

    class Config:
        from_attributes = True
