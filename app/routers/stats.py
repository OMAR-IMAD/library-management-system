from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.database.db import SessionLocal
from app.models.book import Book
from app.models.user import User
from app.models.borrow import Borrow

router = APIRouter()


@router.get("/books")
def total_books():

    db: Session = SessionLocal()

    total = db.query(Book).count()

    db.close()

    return {
        "total_books": total
    }


@router.get("/users")
def total_users():

    db: Session = SessionLocal()

    total = db.query(User).count()

    db.close()

    return {
        "total_users": total
    }


@router.get("/borrows")
def total_borrows():

    db: Session = SessionLocal()

    total_borrows = db.query(Borrow).count()

    active_borrows = db.query(Borrow).filter(
        Borrow.return_date == None
    ).count()

    db.close()

    return {
        "total_borrows": total_borrows,
        "active_borrows": active_borrows
    }