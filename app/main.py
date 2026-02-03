from fastapi import FastAPI
from app.core.database import db
from app.core.base import Base

# IMPORTANT: import models so SQLAlchemy registers them
from app.models import User, Book, Borrow

app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=db.engine)
