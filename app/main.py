from fastapi import FastAPI

from app.database.db import Base, engine

from app.models.book import Book
from app.models.user import User
from app.models.borrow import Borrow
from app.models.reservation import Reservation

from app.routers.users import router as users_router
from app.routers.books import router as books_router
from app.routers.borrow import router as borrow_router
from app.routers.stats import router as stats_router
from app.routers.reservations import router as reservations_router


Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(
    users_router,
    prefix="/users",
    tags=["Users"]
)

app.include_router(
    books_router,
    prefix="/books",
    tags=["Books"]
)

app.include_router(
    borrow_router,
    prefix="/borrow",
    tags=["Borrow"]
)

app.include_router(
    reservations_router,
    prefix="/reservations",
    tags=["Reservations"]
)

app.include_router(
    stats_router,
    prefix="/stats",
    tags=["Statistics"]
)


@app.get("/")
def home():
    return {
        "message": "Library Management System API"
    }