from fastapi import FastAPI , Body
app = FastAPI()

books = [
    {'title': 't1' , 'author':'a1' ,'category': 'c1'},
    {'title': 't2' , 'author':'a2' ,'category': 'c2'},
    {'title': 't3' , 'author':'a3' ,'category': 'c3'},
    {'title': 't4' , 'author':'a4' ,'category': 'c3'},
    {'title': 't5' , 'author':'a5' ,'category': 'c2'}     
         ]
#--------------------------------------------
@app.get('/books')
def read_all_books():
    return books
#uvicorn mainapi:app --reload
#--------------------------------------------
@app.get('/books/{book_title}')
def read_book(book_title):
    for book in books:
        if book.get('title').casefold() == book_title.casefold():
            return book
#http://127.0.0.1:8000/books/t3
#--------------------------------------------
#put : edit data
@app.put('/books/update_book')
def create_book(update_book= Body()):
    for i in range(len(books)):
        if books[i].get('title').casefold() == update_book.get('title').casefold():
            books[i] = update_book
#--------------------------------------------
#delete
@app.delete('/books/delete_book/{book_title}')
def delete_book(book_title:str):
    for i in range(len(books)):
        if books[i].get('title').casefold()== book_title.casefold():
            books.pop(i)
            break
#--------------------------------------------
#query parameter
@app.get('/books/')
def read_category_by_query(category:str):
    books_to_return =[]
    for book in books:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return
#http://127.0.0.1:8000/books/?category=c2
#--------------------------------------------
#post request
@app.get('/books/create_book')
def create_book(new_book = Body()):
    books.append(new_book)
#--------------------------------------------
#http://127.0.0.1:8000/docs#/
#--------------------------------------------
@app.get('/books/{dynamic_param}')
def read_all_books(dynamic_param):
    return {'dynamic_param':dynamic_param}
#http://127.0.0.1:8000/books/harchi%ok%hast
# % = space 