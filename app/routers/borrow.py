from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from app.database.db import SessionLocal
from app.models.borrow import Borrow
from app.models.user import User
from app.models.book import Book
from app.schemas.borrow_schema import (
    BorrowCreate,
    BorrowResponse,
    ReturnBookRequest
)

router = APIRouter()


@router.post("/", response_model=BorrowResponse)
def borrow_book(borrow: BorrowCreate):

    db: Session = SessionLocal()

    user = db.query(User).filter(
        User.id == borrow.user_id
    ).first()

    if not user:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    book = db.query(Book).filter(
        Book.isbn == borrow.book_isbn
    ).first()

    if not book:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    existing_borrow = db.query(Borrow).filter(
        Borrow.book_isbn == borrow.book_isbn,
        Borrow.return_date == None
    ).first()

    if existing_borrow:
        db.close()
        raise HTTPException(
            status_code=400,
            detail="Book is already borrowed"
        )

    new_borrow = Borrow(
        user_id=borrow.user_id,
        book_isbn=borrow.book_isbn
    )

    db.add(new_borrow)
    db.commit()
    db.refresh(new_borrow)

    db.close()

    return new_borrow


@router.post("/return-book")
def return_book(data: ReturnBookRequest):

    db: Session = SessionLocal()

    borrow_record = db.query(Borrow).filter(
        Borrow.user_id == data.user_id,
        Borrow.book_isbn == data.book_isbn,
        Borrow.return_date == None
    ).first()

    if not borrow_record:
        db.close()
        raise HTTPException(
            status_code=404,
            detail="Active borrow record not found"
        )

    borrow_record.return_date = datetime.utcnow()

    db.commit()
    db.refresh(borrow_record)

    db.close()

    return {
        "message": "Book returned successfully"
    }