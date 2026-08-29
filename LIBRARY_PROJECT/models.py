from database import engine
from sqlalchemy import text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column,Session, relationship
from sqlalchemy import ForeignKey

class Base(DeclarativeBase):
    pass

class Author(Base):
    """Models 'authors' table"""
    __tablename__ = 'authors'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] 
    age:Mapped[int]
    books: Mapped[list["Book"]] = relationship(back_populates="author")
    

class Book(Base):
    """Modles 'books' table"""
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] 
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    author: Mapped["Author"] = relationship(back_populates="books")

Base.metadata.create_all(engine)

