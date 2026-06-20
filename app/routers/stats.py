from fastapi import APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func

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

@router.get("/most-borrowed")
def most_borrowed_books():

    db: Session = SessionLocal()

    books = (
        db.query(
            Borrow.book_isbn,
            func.count(Borrow.book_isbn).label("borrow_count")
        )
        .group_by(Borrow.book_isbn)
        .order_by(func.count(Borrow.book_isbn).desc())
        .limit(10)
        .all()
    )

    db.close()

    return books

@router.get("/active-users")
def active_users():

    db: Session = SessionLocal()

    active_users = (
        db.query(Borrow.user_id)
        .filter(Borrow.return_date == None)
        .distinct()
        .count()
    )

    db.close()

    return {
        "active_users": active_users
    }

@router.get("/monthly-borrows")
def monthly_borrows():

    db: Session = SessionLocal()

    borrows = db.query(Borrow).all()

    monthly_data = {}

    for borrow in borrows:

        month = borrow.borrow_date.strftime("%Y-%m")

        if month not in monthly_data:
            monthly_data[month] = 0

        monthly_data[month] += 1

    db.close()

    return monthly_data