from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker ,declarative_base

SQLAlchemy_DataBase_URL = 'sqlite:///./todosApp.db'

engine = create_engine(SQLAlchemy_DataBase_URL , connect_args={'check_same_thread':False})

session_local = sessionmaker(autoflush=False , autocommit = False , bind = engine)

base = declarative_base()

