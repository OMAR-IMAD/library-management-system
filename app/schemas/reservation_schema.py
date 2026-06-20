from pydantic import BaseModel
from datetime import datetime


class ReservationCreate(BaseModel):
    user_id: int
    book_isbn: str


class ReservationResponse(BaseModel):
    id: int
    user_id: int
    book_isbn: str
    reservation_date: datetime
    status: str

    class Config:
        from_attributes = True