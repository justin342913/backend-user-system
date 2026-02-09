from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas.user import UserResponse ,UserCreate
from sqlalchemy.orm import Session
from fastapi import Depends
from app.database import get_db
from app.models.user import User
from app.core.security import get_password_hash
from app.core.security import get_current_user



router = APIRouter(prefix="/users", tags=["users"])



@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    new_user = User(
        email=user.email,
        hashed_password=get_password_hash(user.password),
        is_active=True
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user
