from sqlalchemy.orm import Session
from app.models.user import User
from app.repositories.user import UserRepository
from fastapi import Depends


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def create_user(
        self,
        username: str,
        email: str,
        hashed_password: str
    ) -> User:
        user = User(
            username=username,
            email=email,
            hashed_password=hashed_password,
        )
        return self.user_repo.create(user)
    
    def get_user_by_id(self, user_id: int) -> User | None:
        return self.user_repo.get_by_id(user_id)
    
    def get_users(self) -> list[User]:
        return self.user_repo.get_all()
    