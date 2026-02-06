from fastapi import FastAPI

from app.api.user import router as user_router
from app.api.book import router as book_router
from app.api.borrow import router as borrow_router
from app.api.LLM_router import router as llm_router
# @app.on_event("startup")
# def on_startup():
#     Base.metadata.create_all(bind=db.engine)


app = FastAPI(title="Library System API")
@app.get("/ping")
def ping():
    return {"ok": True}
app.include_router(user_router)
app.include_router(book_router)
app.include_router(borrow_router)
app.include_router(llm_router)

