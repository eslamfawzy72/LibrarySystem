from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user import UserService

router = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_user(
    user: UserCreate,
    user_service: UserService = Depends(),
):
 
        return user_service.create_user(
            username=user.username,
            email=user.email,
            hashed_password=user.password,  # hashing later
        )

@router.get(
    "/{user_id}",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
)
def get_user(
    user_id: int,
    user_service: UserService = Depends()
):
    user = user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get(
    "",
    response_model=list[UserResponse],
    status_code=status.HTTP_200_OK,
)
def get_users(
    user_service: UserService = Depends()
):
    return user_service.get_users()