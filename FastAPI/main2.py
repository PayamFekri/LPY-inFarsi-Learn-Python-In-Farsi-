from fastapi import FastAPI , Body
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class Book:
    id : int 
    title : str 
    author : str 
    description : str
    rating : int
    
    def __init__(self, id , title , author , descripttion ,rating):
        self.id = id 
        self.title = title
        self.author = author
        self.description = descripttion
        self.rating = rating

class BookRequest(BaseModel):
    id : Optional[int]= None 
    title : str = Field(min_length= 2)
    author : str = Field(min_length= 1)
    description : str= Field(min_length= 1 , max_length= 100)
    rating : int = Field(gt=0 , lt=10)


books= [
    Book(1,'ce' , 'payam' , 'the best book..' , 2),
    Book(2,'ce' , 'sohrab' , 'the best book..' , 5),
    Book(3,'py programming' , 'payam' , 'the best book..' , 3),
    Book(4,'ce' , 'payam' , 'the best book..' , 4),
    Book(5,'ml' , 'payam' , 'the best book..' , 7),
    Book(6,'ce' , 'payam' , 'the best book..' , 5),
    Book(7,'dl' , 'mary' , 'the best book..' , 9),
    Book(8,'dl' , 'ali' , 'the best book..' , 12),
]



@app.get('/books2')
def read_all_books():
    return books
#uvicorn main2:app --reload         : ->on your commands

@app.post("/create-book")
def create_book(book_request : BookRequest):
    new_book = Book(book_request.model_dump())
    books.append((new_book))
    
def find_book_id(book: Book):
    book.id= 0 if len(books) == 0 else books[-1].id+1
    return book