from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.database.db import Base


class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, nullable=False)

    book_isbn = Column(String, nullable=False)

    reservation_date = Column(
        DateTime,
        default=datetime.utcnow
    )

    status = Column(
        String,
        default="active"
    )