from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from typing import Generator
from app.core.config import get_settings

Base = declarative_base()


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

    def session(self) -> Generator[Session, None, None]:
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()


_db = Database()  # private singleton


def get_db() -> Generator[Session, None, None]:
    yield from _db.session()
