from fastapi import FastAPI
import model 
from data import engine
from routers import auth , todos

app = FastAPI()
model.base.metadata.create_all(bind = engine)


app.include_router(auth.router)
app.include_router(todos.router)


# uvicorn main:app --reload 
# sqlite3 todos.db

# http://127.0.0.1:8000/docs#