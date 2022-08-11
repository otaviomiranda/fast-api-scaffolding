from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    first_name: str
    last_name: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str
