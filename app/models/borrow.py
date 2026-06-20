from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timedelta

from app.database.db import Base


class Borrow(Base):
    __tablename__ = "borrows"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, nullable=False)

    book_isbn = Column(String, nullable=False)

    borrow_date = Column(
        DateTime,
        default=datetime.utcnow
    )

    due_date = Column(
        DateTime,
        default=lambda: datetime.utcnow() + timedelta(days=14)
    )

    return_date = Column(
        DateTime,
        nullable=True
    )

    status = Column(
        String,
        default="borrowed"
    )