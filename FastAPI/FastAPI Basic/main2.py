from fastapi import FastAPI , Body, Path , Query ,HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from starlette import status

app = FastAPI()

class Book:
    id : int 
    title : str 
    author : str 
    description : str
    rating : int 
    year : int
    
    def __init__(self, id , title , author , descripttion ,rating,year):
        self.id = id 
        self.title = title
        self.author = author
        self.description = descripttion
        self.rating = rating
        self.year = year

class BookRequest(BaseModel):
    id : Optional[int]= None 
    title : str = Field(min_length= 2)
    author : str = Field(min_length= 1)
    description : str= Field(min_length= 1 , max_length= 100)
    rating : int = Field(gt=0 , lt=10)
    year :int = Field(gt = 1999,lt=2031)


books= [
    Book(1,'ce' , 'payam' , 'the best book..' , 2,2001),
    Book(2,'ce' , 'sohrab' , 'the best book..' , 5,2005),
    Book(3,'py programming' , 'payam' , 'the best book..' , 3, 2015),
    Book(4,'ce' , 'payam' , 'the best book..' , 4,2010),
    Book(5,'ml' , 'payam' , 'the best book..' , 7,2014),
    Book(6,'ce' , 'payam' , 'the best book..' , 5,2022),
    Book(7,'dl' , 'mary' , 'the best book..' , 9,2023),
    Book(8,'dl' , 'ali' , 'the best book..' , 7,2027),
]



@app.get('/books2', status_code= status.HTTP_200_OK)
def read_all_books():
    return books
#uvicorn main2:app --reload         : ->on your commands

@app.get("/books2/{book_id}", status_code= status.HTTP_200_OK)
async def read_book(book_id:int = Path(gt=0)):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404 , detail='item not found')


@app.get("/books2/", status_code= status.HTTP_200_OK)
def read_book_by_rating(book_rating: int = Query(gt=0 , lt=8)):
    book_to_return = []
    for book in books:
        if book.rating == book_rating:
            book_to_return.append(book)
    return book_to_return



@app.post("/create-book", status_code= status.HTTP_201_CREATED)
def create_book(book_request : BookRequest):
    new_book = Book(**book_request.model_dump())
    books.append((new_book))
    
def find_book_id(book: Book):
    book.id= 0 if len(books) == 0 else books[-1].id+1
    return book



@app.put("/books2/update_books", status_code= status.HTTP_204_NO_CONTENT)
def update_book(book:BookRequest):
    book_changed = False
    for i in range (len(books)):
        if books[i].id == book.id:
            books[i] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404  , detail='item not found')
            
@app.delete("/books_del/{book_id}", status_code= status.HTTP_204_NO_CONTENT)
def delete_book(book_id:int = Path(gt=0)):
    for i in range (len(books)):
        if books[i].id == book_id:
            books.pop(i)
            break


@app.get("/books2/publish/", status_code= status.HTTP_200_OK)
async def read_book_publish_date(year: int = Query(gt=1999, lt=2031)):
    return_books = []
    for book in books:
        if book.year == year:
            return_books.append(book)
    return return_books
            
#http://127.0.0.1:8000/docs#/
