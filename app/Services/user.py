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
    def get_user_by_id(self, db: Session, user_id: int) -> User | None:
        return self.user_repo.get_by_id(db, user_id)
    def get_users(self, db: Session) -> list[User]:
        return db.query(User).all()
    