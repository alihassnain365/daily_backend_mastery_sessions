from database import engine, Session
from models import Author, Book
from sqlalchemy import select

with Session(engine) as session:
    if session.execute(select(Author)).scalars().all():
        print("Seed alreay exists, so skiping this time")
    else:
        for i in range(1,11):
            author = Author(name=f"autho{i}", age=i*10)
            for j in range(1,3):
                book = Book(title = f"book{j}")
                author.books.append(book)
            session.add(author)
        session.commit()
        