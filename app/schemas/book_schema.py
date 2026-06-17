from pydantic import BaseModel


class BookCreate(BaseModel):
    isbn: str
    title: str
    author: str
    publisher: str | None = None
    publication_year: int | None = None


class BookResponse(BaseModel):
    isbn: str
    title: str
    author: str
    publisher: str | None = None
    publication_year: int | None = None

    class Config:
        from_attributes = True