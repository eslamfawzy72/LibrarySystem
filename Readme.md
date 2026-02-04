# Library System API

A clean, scalable **Library Management System backend** built with **FastAPI** and **PostgreSQL**, following clean architecture and backend best practices.

---

## Features

- User management (students)
- Book management
- Borrow and return books with business rules
- Service layer for domain logic
- Repository pattern for database access
- Fully documented API using OpenAPI / ReDoc

---

## Architecture

This project follows a layered architecture:

app/
├── api/ # FastAPI routers (HTTP layer)
├── services/ # Business logic
├── repositories/ # Database access layer
├── models/ # SQLAlchemy ORM models
├── schemas/ # Pydantic schemas (DTOs)
├── core/ # Config & database setup
└── main.py # Application entry point


Why this architecture:
- Clear separation of concerns
- Easy to test and maintain
- Scales well as the system grows

---

## Tech Stack

- Python 3.12
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Uvicorn

---

## API Documentation

Swagger UI:
http://127.0.0.1:8000/docs


ReDoc:
http://127.0.0.1:8000/redoc


---

## API Endpoints

### Users

| Method | Endpoint | Description |
|------|--------|------------|
| GET | `/users` | List all users |
| GET | `/users/{user_id}` | Get user by ID |
| POST | `/users` | Create a new user |

---

### Books

| Method | Endpoint | Description |
|------|--------|------------|
| GET | `/books` | List all books |
| GET | `/books/{book_id}` | Get book by ID |
| GET | `/books/title/{title}` | Get book by title |
| POST | `/books` | Create a new book |

---

### Borrows

| Method | Endpoint | Description |
|------|--------|------------|
| POST | `/borrows` | Borrow a book |
| POST | `/borrows/{borrow_id}/return` | Return a borrowed book |

---

## Example: Borrow a Book

```bash
curl -X POST http://127.0.0.1:8000/borrows \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1,
    "book_id": 4,
    "start_date": "2026-02-03T14:28:58Z",
    "return_date": "2026-02-10T14:28:58Z"
  }'
Setup and Run
1. Clone the repository
git clone https://github.com/eslamfawzy72/LibrarySystem
cd LibrarySystem
2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
4. Configure environment variables
Create a .env file:

DATABASE_URL=postgresql://postgres:password@localhost:5432/library_db
5. Run the server
uvicorn app.main:app --reload
Business Rules
A book cannot be borrowed if no copies are available

A user cannot borrow the same book twice at the same time

Borrow duration is validated in the service layer

Returning a book restores availability automatically

Code Quality Principles
No business logic in routes

No database logic in services

No ORM models exposed in API responses

Clean commit history

.gitignore configured correctly

Future Improvements
Authentication and authorization (JWT)

Password hashing

Unit and integration tests

Pagination and filtering

Borrow due dates and penalties

Author
Eslam Mohamed Fawzy
Faculty of Engineering – Computer and AI
Backend Developer (FastAPI)
