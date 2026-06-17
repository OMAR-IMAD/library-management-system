from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.database.db import SessionLocal
from app.models.user import User
from app.schemas.user_schema import UserCreate, UserResponse

router = APIRouter()


@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate):
    db: Session = SessionLocal()

    new_user = User(
        student_number=user.student_number,
        username=user.username,
        email=user.email,
        password=user.password,
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.close()

    return new_user


@router.get("/", response_model=list[UserResponse])
def get_users():
    db: Session = SessionLocal()

    users = db.query(User).all()

    db.close()

    return users