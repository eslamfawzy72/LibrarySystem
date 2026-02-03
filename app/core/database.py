from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from typing import Generator
from app.core.config import get_settings


class Database:
    def __init__(self) -> None:
        settings = get_settings()

        self.engine = create_engine(
            settings.DATABASE_URL,
            echo=True,
            future=True,
        )

        self.SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine,
        )

    def get_session(self) -> Generator[Session, None, None]:
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()


db = Database()
Base = declarative_base()
