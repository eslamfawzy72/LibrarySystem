from sqlalchemy.orm import Session
from app.models.user import User
from app.repositories.user import UserRepository


class UserService:
    def __init__(self):
        self.user_repo = UserRepository()

    def create_user(
        self, db: Session, username: str, email: str, hashed_password: str
    ) -> User:
        user = User(
            username=username,
            email=email,
            hashed_password=hashed_password,
        )
        return self.user_repo.create(db, user)
