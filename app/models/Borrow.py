from sqlalchemy import Column, Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.base import Base

class Borrow(Base):
    __tablename__ = "borrows"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    start_date = Column(DateTime, nullable=False)
    return_date = Column(DateTime, nullable=True)
    is_returned = Column(Boolean, default=False)  # New field to track return status

    user = relationship("User", back_populates="borrows")
    book = relationship("Book", back_populates="borrows")