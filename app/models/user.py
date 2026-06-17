from sqlalchemy import Column, Integer, String
from app.database.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    student_number = Column(String, unique=True, nullable=False)

    username = Column(String, nullable=False, unique=True)

    email = Column(String, nullable=False, unique=True)

    password = Column(String, nullable=False)

    role = Column(String, nullable=False, default="student")