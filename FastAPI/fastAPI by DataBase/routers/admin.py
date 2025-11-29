from fastapi import APIRouter, Depends, HTTPException, Path
import model
from data import session_local
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from .auth import get_current_user

router = APIRouter(prefix='/admin' ,
                   tags= ['admin'])

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.get("/todo", status_code=status.HTTP_200_OK)
def read_all(user:user_dependency ,db: db_dependency):
    if user is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code=401, detail="Authentication Failed")
    return db.query(model.Todo).all()

@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(user:user_dependency ,db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(model.Todo).filter(model.Todo.id == todo_id).first()
    if todo_model is None or user.get('user_role') != 'admin':
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo_model)
    db.commit()