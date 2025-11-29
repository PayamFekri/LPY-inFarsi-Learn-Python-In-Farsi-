from datetime import timedelta , datetime, timezone
from fastapi import APIRouter, Depends ,HTTPException
from pydantic import BaseModel
from passlib.context import CryptContext
from data import session_local
from typing import Annotated
from sqlalchemy.orm import Session
from model import Users
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm , OAuth2PasswordBearer
from jose import jwt , JWTError
# todosApp.db

router = APIRouter(prefix='/auth' , tags= ['auth'])

secret_key ='4d61d53a713655431fd335cab06ee9fd6cdcf7cb2593b863b5fa6203efcafebd' 
algorithm_hash = 'HS256'
bcrypt_context = CryptContext(schemes=['bcrypt'] , deprecated = 'auto')
oAuth2Bearer = OAuth2PasswordBearer(tokenUrl='auth/token')
 
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

def authenticate_user(username:str , password:str , db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password , user.hashed_password):
        return False
    return user

def create_access_token(username:str , userID:int , role : str ,expires_delta:timedelta):
    encode = {'sub': username , 'ID' : userID , 'role' : role}
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp':expires})
    return jwt.encode(encode , secret_key , algorithm= algorithm_hash)
    
def get_current_user(token:Annotated[str , Depends(oAuth2Bearer)]):
    try : 
        payload = jwt.decode(token , secret_key , algorithms=[algorithm_hash])
        username :str = payload.get('sub')
        userID : int = payload.get('ID')
        user_role : str = payload.get('role')
        if username is None or userID is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail='could not validate user.')
        return {'username' : username , 'ID' : userID , 'user_role' : user_role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail='could not validate user.')


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
def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='could not validate user.')
    token = create_access_token(user.username, user.id,user.role, timedelta(minutes=20))
    return {"access_token": token, "token_type": "bearer"}
