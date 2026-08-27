from fastapi import FastAPI, Depends, HTTPException
from database import Session, sessionLocal
from models import Author, Book
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError


app = FastAPI()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

class AuthorOut(BaseModel):
    id: int
    name: str
    age: int

class BookCreate(BaseModel):
    title: str
    author_id: int

class BookOut(BaseModel):
    id: int
    title: str
    author_id:int

"""1. getting author """

@app.get("/get_author/{author_id}", response_model=AuthorOut)
def get_author(author_id: int, db= Depends(get_db)):
    author = db.get(Author, author_id)
    if author is None:
        raise HTTPException(status_code=404, detail="Id does not exists.")
    else:
        return author

"""2. posting a book"""

@app.post("/book/create_book", response_model=BookOut)
def create_book(book: BookCreate, db:Session = Depends(get_db)):
    try:
        new_book = Book(
            title = book.title,
            author_id = book.author_id
        )
        db.add(new_book)
        db.commit()
        return new_book
    except IntegrityError as e:
        print(f"The following error happened", e)
        raise HTTPException(status_code=400, detail="Invalid aturho_id")
    

"""3. getting book"""

@app.get("/book/get_book/{book_id}", response_model=BookOut)
def get_book(book_id: int, db:Session = Depends(get_db)):
    book = db.get(Book,book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book with this id not exists.")
    else:
        return book    

    


