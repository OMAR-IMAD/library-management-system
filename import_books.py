import pandas as pd
from sqlalchemy.orm import Session

from app.database.db import SessionLocal
from app.models.book import Book

db: Session = SessionLocal()

df = pd.read_csv(
    "books.csv",
    sep=";",
    encoding="latin1",
    on_bad_lines="skip",
    low_memory=False
)

count = 0

for _, row in df.iterrows():

    isbn = str(row["ISBN"])

    existing_book = db.query(Book).filter(
        Book.isbn == isbn
    ).first()

    if existing_book:
        continue

    try:
        year = int(row["Year-Of-Publication"])
    except:
        year = 0

    book = Book(
        isbn=isbn,
        title=str(row["Book-Title"]),
        author=str(row["Book-Author"]),
        publisher=str(row["Publisher"]),
        publication_year=year
    )

    db.add(book)

    count += 1

    if count % 1000 == 0:
        db.commit()
        print(f"{count} books imported")

db.commit()

print(f"Finished importing {count} books")

db.close()