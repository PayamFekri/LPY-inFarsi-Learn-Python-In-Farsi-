from sqlalchemy import Column ,Integer, String, Boolean , ForeignKey
from data import base

class Users(base):
    __tablename__ = 'users'
    
    id = Column(Integer , primary_key= True , index = True)
    Email = Column(String, unique = True)
    UserName = Column(String, unique = True)
    first_name= Column(String)
    last_name = Column(String , default=False)
    hashed_password = Column(String)
    is_active = Column(Boolean , default= True)
    role = Column(String)

class Todo(base):
    __tablename__ = 'todos'
    
    id = Column(Integer , primary_key= True , index = True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean , default=False)
    ownerID = Column(Integer , ForeignKey("users.id"))