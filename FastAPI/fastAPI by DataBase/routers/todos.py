from fastapi import APIRouter, Depends, HTTPException, Path
import model
from data import session_local
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from pydantic import BaseModel, Field
from .auth import get_current_user

router = APIRouter()

# uvicorn main:app --reload 
# sqlite3 todos.db

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool



@router.get("/", status_code=status.HTTP_200_OK)
def read_all(user:user_dependency ,db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    return db.query(model.Todo).filter(model.Todo.owner_id ==user.get('ID')).all()




@router.get("/todos/{todo_id}", status_code=status.HTTP_200_OK)
def read_todo(user:user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(model.Todo).filter(model.Todo.id == todo_id).filter(model.Todo.owner_id ==user.get('ID')).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail="Todo not found")

@router.post("/todo/", status_code=status.HTTP_201_CREATED)
def create_todo(user: user_dependency, db: db_dependency, todo_request: TodoRequest):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    
    todo_model = model.Todo(**todo_request.model_dump(), owner_id=user.get('ID'))
    db.add(todo_model)
    db.commit()
    db.refresh(todo_model)
    return todo_model

@router.put("/todo/{todo_id}", status_code=status.HTTP_200_OK)
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
    db.refresh(todo_model)
    return todo_model

@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(model.Todo).filter(model.Todo.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo_model)
    db.commit()
