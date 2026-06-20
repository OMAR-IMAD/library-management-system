from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.database.db import SessionLocal
from app.models.reservation import Reservation
from app.models.book import Book
from app.models.user import User

from app.schemas.reservation_schema import (
    ReservationCreate,
    ReservationResponse
)

router = APIRouter()


@router.post("/", response_model=ReservationResponse)
def create_reservation(data: ReservationCreate):

    db: Session = SessionLocal()

    user = db.query(User).filter(
        User.id == data.user_id
    ).first()

    if not user:
        db.close()

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    book = db.query(Book).filter(
        Book.isbn == data.book_isbn
    ).first()

    if not book:
        db.close()

        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    reservation = Reservation(
        user_id=data.user_id,
        book_isbn=data.book_isbn,
        status="active"
    )

    db.add(reservation)
    db.commit()
    db.refresh(reservation)

    db.close()

    return reservation


@router.get("/", response_model=list[ReservationResponse])
def get_reservations():

    db: Session = SessionLocal()

    reservations = db.query(
        Reservation
    ).all()

    db.close()

    return reservations


@router.delete("/{reservation_id}")
def cancel_reservation(reservation_id: int):

    db: Session = SessionLocal()

    reservation = db.query(
        Reservation
    ).filter(
        Reservation.id == reservation_id
    ).first()

    if not reservation:
        db.close()

        raise HTTPException(
            status_code=404,
            detail="Reservation not found"
        )

    db.delete(reservation)
    db.commit()

    db.close()

    return {
        "message": "Reservation cancelled successfully"
    }