from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    is_active: bool


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True
