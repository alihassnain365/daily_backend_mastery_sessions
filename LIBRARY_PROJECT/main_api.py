from fastapi import FastAPI, Depends, HTTPException
from database import engine, sessionLocal
from models import Author, Book
from pydantic import BaseModel

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

@app.get("/get_author/{author_id}", response_model=AuthorOut)
def get_author(author_id: int, db= Depends(get_db)):
    author = db.get(Author, author_id)
    if author is None:
        raise HTTPException(status_code=404, detail="Id does not exists.")
    else:
        return author
