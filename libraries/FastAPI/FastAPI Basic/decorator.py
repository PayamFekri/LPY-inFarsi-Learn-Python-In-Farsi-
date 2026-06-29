from fastapi import FastAPI , Request ,Depends, HTTPException
from matplotlib.pyplot import stem
import time 
from fastapi.security import OAuth2PasswordBearer
from functools import wraps

app = FastAPI()

@app.get("/items/")
async def list_items():
    return {"items": []}

@app.post("/items/")
async def create_item(item: stem):
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: stem):
    return item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"deleted": item_id}

@app.patch("/items/{item_id}")
async def partial_update(item_id: int):
    ...

@app.middleware("http")
async def add_process_time(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    process_time = time.time() - start
    response.headers["X-Process-Time"] = str(process_time)
    return response

# deprecated decorator!!!!
@app.on_event("startup")
async def startup_event():
    # اتصال به دیتابیس، لود مدل ML و ...
    pass

@app.on_event("shutdown")
async def shutdown_event():
    pass

#New decorator design : 
from contextlib import asynccontextmanager
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    # اینجا کارهای startup مثل اتصال دیتابیس، لود مدل و ...
    yield
    # اینجا کارهای shutdown مثل بستن connection ها
    print("Shutting down...")
app = FastAPI(lifespan=lifespan)


# Depends — Dependency Injection
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = verify_token(token)
    if not user:
        raise HTTPException(status_code=401)
    return user

@app.get("/me")
async def read_me(current_user = Depends(get_current_user)):
    return current_user


# Custom Decorator
def admin_only(func):
    @wraps(func)
    async def wrapper(*args, current_user=Depends(get_current_user), **kwargs):
        if not current_user.is_admin:
            raise HTTPException(status_code=403, detail="دسترسی ندارید")
        return await func(*args, **kwargs)
    return wrapper

@app.get("/admin/users")
@admin_only
async def list_users():
    ...