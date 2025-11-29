from fastapi import APIRouter, Depends, HTTPException, Path
import model
from data import session_local
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from pydantic import BaseModel, Field
from .auth import get_current_user
from passlib.context import CryptContext
router = APIRouter(prefix='/user' ,
                   tags= ['user'])

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]
bcrypt_context = CryptContext(schemes=['bcrypt'] , deprecated = 'auto')

class UserVerification(BaseModel):
    password : str
    new_password :str = Field(min_length=6)

@router.get("/" , status_code= status.HTTP_200_OK)
def get_user(user : user_dependency , db:db_dependency):
    if user is None:
        raise HTTPException(status_code=401 , detail='Authentication Failed')
    return db.query(model.Users).filter(model.Users.id == user.get('id')).first()


@router.put("/password" , status_code= status.HTTP_204_NO_CONTENT)
def change_password(user: user_dependency , db : db_dependency , userverify : UserVerification):
    if user is None:
        raise HTTPException(status_code=401 , detail='Authentication Failed')
    user_model = db.query(model.Users).filter(model.Users.id == user.get('ID')).first()
    if not bcrypt_context.verify(userverify.password , user_model.hashed_password):
        raise HTTPException(status_code=401 , detail='ERROR on Password Change')
    user_model.hashed_password = bcrypt_context.hash(userverify.new_password)
    db.add(user_model)
    db.commit()