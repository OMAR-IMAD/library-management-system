from sqlalchemy import Column, String, Integer
from app.database.db import Base


class Book(Base):
    __tablename__ = "books"

    isbn = Column(String, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    publisher = Column(String)
    publication_year = Column(Integer)