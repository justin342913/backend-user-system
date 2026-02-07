from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas.user import UserResponse ,UserCreate

router = APIRouter(prefix="/users", tags=["users"])


fake_users = [
    {"id": 1, "email": "test1@example.com", "is_active": True},
    {"id": 2, "email": "test2@example.com", "is_active": False},
]

@router.get("/", response_model=List[UserResponse])
def get_users():
    return fake_users


@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_user(user: UserCreate):
    for u in fake_users:
        if u["email"] == user.email:
          raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    new_user = {
        "id": len(fake_users) + 1,
        "email": user.email,
        "is_active": True,
    }
    fake_users.append(new_user)
    return new_user