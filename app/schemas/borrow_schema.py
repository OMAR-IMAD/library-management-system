from pydantic import BaseModel
from datetime import datetime


class BorrowCreate(BaseModel):
    user_id: int
    book_isbn: str


class BorrowResponse(BaseModel):
    id: int
    user_id: int
    book_isbn: str
    borrow_date: datetime
    return_date: datetime | None = None

    class Config:
        from_attributes = True


class ReturnBookRequest(BaseModel):
    user_id: int
    book_isbn: str