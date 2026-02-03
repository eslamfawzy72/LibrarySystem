from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
 
class UserBase(BaseModel):
    username: str = Field(
        ...,
        min_length=3,
        max_length=20,
        description="Unique username"
    )
    email: EmailStr = Field(
        ...,
        description="User email address"
    )
class UserCreate(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        description="Plain password (will be hashed)"
    )
    
class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
