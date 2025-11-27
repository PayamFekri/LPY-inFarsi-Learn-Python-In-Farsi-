from fastapi import APIRouter

router = APIRouter()

@router.get("/auth/")
def get_user():
    return {'user':'authenticated'}