from fastapi import FastAPI, Depends, HTTPException
from database import Session, sessionLocal
from models import Author, Book
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError
from sqlalchemy import text, select



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

class BookPut(BaseModel):
    title: str | None = None
    cost: int | float | None = None
    author_id: int | None = None


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

"""3.1  getting all books inside book"""

@app.get("/get/books", response_model=list[BookOut])
def get_all_books(price_max: int | None = None, price_min: int | None = None, author_id: int | None = None, limit: int = 10, offset: int = 0, db: Session = Depends(get_db)):
    query = select(Book)
    if author_id is not None:
        query = query.where(Book.author_id == author_id)
    if price_min is not None:
        query = query.where(Book.cost >= price_min)
    if price_max is not None:
        query = query.where(Book.cost <= price_max)
    query = query.order_by(Book.cost.desc()).limit(limit).offset(offset)
    books = db.execute(query).scalars().all()
    return books


"""4. updating book"""  

@app.put("/book/update/{book_id}", response_model=BookOut)
def put_book(book_id:int , book: BookPut, db: Session = Depends(get_db)):
    targeted_book = db.get(Book, book_id)
    if targeted_book is None:
        raise HTTPException(status_code=404, detail="Book is not found with this id")
    if book.title is not None:
        targeted_book.title = book.title
    if book.cost is not None:
        targeted_book.cost = book.cost
    if book.author_id is not None:
        targeted_book.author_id = book.author_id

    try:
        db.commit()
    except IntegrityError as e:
        print(f"The following error has occured: {e}")
        raise HTTPException(status_code=400, detail="Invalid author_id")
    return targeted_book

"""5. deleting book"""

@app.delete("/book/delete/{book_id}", status_code=204)
def del_book(book_id: int, db: Session = Depends(get_db)):
    targeted_book = db.get(Book, book_id)
    if targeted_book is None:
        raise HTTPException(status_code=404, detail="Book with this id doesn't exist.")
    db.delete(targeted_book)
    db.commit()


        

    


