from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.database.db import SessionLocal
from app.models.book import Book
from app.schemas.book_schema import BookCreate, BookResponse

router = APIRouter()


@router.post("/", response_model=BookResponse)
def create_book(book: BookCreate):
    db: Session = SessionLocal()

    new_book = Book(
        isbn=book.isbn,
        title=book.title,
        author=book.author,
        publisher=book.publisher,
        publication_year=book.publication_year
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    db.close()

    return new_book


@router.get("/", response_model=list[BookResponse])
def get_books(
    page: int = 1,
    limit: int = 10
):
    db: Session = SessionLocal()

    skip = (page - 1) * limit

    books = db.query(Book)\
        .offset(skip)\
        .limit(limit)\
        .all()

    db.close()

    return books


@router.get("/search/")
def search_books(query: str):

    db: Session = SessionLocal()

    books = db.query(Book).filter(
        (Book.title.contains(query)) |
        (Book.author.contains(query))
    ).all()

    db.close()

    return books


@router.get("/{isbn}", response_model=BookResponse)
def get_book(isbn: str):
    db: Session = SessionLocal()

    book = db.query(Book).filter(Book.isbn == isbn).first()

    db.close()

    return book


@router.delete("/{isbn}")
def delete_book(isbn: str):
    db: Session = SessionLocal()

    book = db.query(Book).filter(Book.isbn == isbn).first()

    if not book:
        db.close()
        return {"message": "Book not found"}

    db.delete(book)
    db.commit()

    db.close()

    return {"message": "Book deleted successfully"}


@router.put("/{isbn}", response_model=BookResponse)
def update_book(isbn: str, updated_book: BookCreate):
    db: Session = SessionLocal()

    book = db.query(Book).filter(Book.isbn == isbn).first()

    if not book:
        db.close()
        return {"message": "Book not found"}

    book.isbn = updated_book.isbn
    book.title = updated_book.title
    book.author = updated_book.author
    book.publisher = updated_book.publisher
    book.publication_year = updated_book.publication_year

    db.commit()
    db.refresh(book)

    db.close()

    return book