from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from passlib.context import CryptContext
from data import session_local
from typing import Annotated
from sqlalchemy.orm import Session
from model import Users
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()
bcrypt_context = CryptContext(schemes=['bcrypt'] , deprecated = 'auto')

class CreateUserRequest(BaseModel):
    username: str 
    email : str 
    first_name : str
    last_name : str 
    password : str
    role : str

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session , Depends(get_db)]



@router.post("/auth/" , status_code = status.HTTP_201_CREATED)
def create_user(db:db_dependency,
                create_user_request : CreateUserRequest):
    
    
    create_user_request = Users(
    email=create_user_request.email,
    username=create_user_request.username,
    first_name=create_user_request.first_name,
    last_name=create_user_request.last_name,
    hashed_password=bcrypt_context.hash(create_user_request.password),
    is_active=True,
    role=create_user_request.role
    )
    db.add(create_user_request)
    db.commit()
    
@router.post("/token")
def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm , Depends()] , db:db_dependency):
    return 'token'
