from sqlalchemy import create_engine, ForeignKey, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship, selectinload

engine = create_engine("sqlite:///:memory:",echo=True)

class Base(DeclarativeBase):
    pass

class Author(Base):
    """Models 'authors' table"""
    __tablename__ = 'authors'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    books: Mapped[list["Book"]] = relationship(back_populates='author')


class Book(Base):
    """Models 'books' tables"""
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    author: Mapped["Author"] = relationship(back_populates='books')

# ---- creating the tables from that structure

Base.metadata.create_all(engine)

with Session(engine) as session:
    for i in range(1,11):
        author = Author(name = f"author{i}")
        for j in range(1,3):
            book = Book(name=f"book{j}")
            author.books.append(book)
        session.add(author)
    session.commit()


"""Lazy loading"""
# 11 - select statements ran
with Session(engine) as session:
    stmt = select(Author)
    authors = session.execute(stmt).scalars().all()
    for author in authors:
        print(author.name, author.books)


"""Eager loadint - selectinload"""
with Session(engine) as session:
# 2 - select statements ran
    stmt = select(Author).options(selectinload(Author.books))
    authors = session.execute(stmt).scalars().all()
    for author in authors:
        print(author.name, author.books)

