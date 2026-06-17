from pydantic import BaseModel


class UserCreate(BaseModel):
    student_number: str
    username: str
    email: str
    password: str
    role: str = "student"


class UserResponse(BaseModel):
    id: int
    student_number: str
    username: str
    email: str
    role: str

    class Config:
        from_attributes = True