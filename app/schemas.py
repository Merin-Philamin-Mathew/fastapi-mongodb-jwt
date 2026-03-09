from datetime import datetime
from typing import Annotated
from pydantic import BaseModel, EmailStr, StringConstraints


class UserBaseSchema(BaseModel):
    name: str
    email: str
    photo: str
    role: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        # orm_mode = True #showing pydantic warning
        from_attributes = True


class CreateUserSchema(UserBaseSchema):
    password: Annotated[str, StringConstraints(min_length=8)]
    passwordConfirm: str
    verified: bool = False


class LoginUserSchema(BaseModel):
    email: EmailStr
    password: Annotated[str, StringConstraints(min_length=8)]


class UserResponseSchema(UserBaseSchema):
    id: str
    pass


class UserResponse(BaseModel):
    status: str
    user: UserResponseSchema

