from fastapi import APIRouter
from typing import List
from app.schemas.user import UserResponse

router = APIRouter(prefix="/users", tags=["users"])


fake_users = [
    {"id": 1, "email": "test1@example.com", "is_active": True},
    {"id": 2, "email": "test2@example.com", "is_active": False},
]

@router.get("/", response_model=List[UserResponse])
def get_users():
    return fake_users
