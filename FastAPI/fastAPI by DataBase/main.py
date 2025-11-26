from fastapi import FastAPI , Depends ,HTTPException , Path
import model 
from data import engine, session_local
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from pydantic import BaseModel , Field


app = FastAPI()
model.base.metadata.create_all(bind = engine)

# uvicorn main:app --reload 
# sqlite3 todos.db

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session , Depends(get_db)]

class TodoRequest(BaseModel):
    title : str = Field(min_length= 3)
    description : str = Field(min_length= 3 , max_length= 100)
    priority : int = Field (gt= 0 , lt= 6)
    complete : bool

@app.get("/")
def read_all(db:db_dependency):
    return db.query(model.Todo).all()

@app.get("/todos/{todos_id}" , status_code= status.HTTP_200_OK)
def read_todo(db:db_dependency , todo_id:int = Path( gt = 0)):
    todos_model = db.query(model.Todo).filter(model.Todo.id == todo_id).first()
    if todos_model is not None:
        return todos_model
    raise HTTPException(status_code= 404 , detail= 'Todo not found')


@app.post("/todo/" ,status_code= status.HTTP_201_CREATED) #handler
def create_todo(db:db_dependency ,todo_request: TodoRequest):
    todo_model = model.Todo(**todo_request.model_dump())
    db.add(todo_model)
    db.commit()
    
    

@app.put("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def update_todo(db: db_dependency, todo_id: int, todo_request: TodoRequest):
    todo_model = db.query(model.Todo).filter(model.Todo.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")

    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete

    db.add(todo_model)
    db.commit()

@app.delete("/todo/{todo_id}" , status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model =db.query(model.Todo).filter(model.Todo.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.query(model.Todo).filter(model.Todo.id == todo_id).delete()
    db.commit()

# http://127.0.0.1:8000/docs#