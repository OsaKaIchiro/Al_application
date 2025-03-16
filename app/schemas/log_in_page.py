from pydantic import BaseModel
from typing import Union, Optional, Any

class UserResponse(BaseModel):
    username: str

class LoginResponse(BaseModel):
    success: bool
    username: Optional[str] = None

class NewUserResponse(BaseModel):
    success1: bool
    success2: bool

class UserAndPassword(UserResponse):
    password: str = None