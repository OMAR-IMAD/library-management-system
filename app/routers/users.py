from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.database.db import SessionLocal
from app.models.user import User
from app.schemas.user_schema import (
    UserCreate,
    UserResponse,
    UserLogin
)

from app.auth.auth_handler import (
    hash_password,
    verify_password,
    create_access_token
)

router = APIRouter()


@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate):

    db: Session = SessionLocal()

    hashed_password = hash_password(
        user.password
    )

    new_user = User(
        student_number=user.student_number,
        username=user.username,
        email=user.email,
        password=hashed_password,
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    db.close()

    return new_user


@router.post("/login")
def login_user(user: UserLogin):

    db: Session = SessionLocal()

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not existing_user:
        db.close()

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(
        user.password,
        existing_user.password
    ):
        db.close()

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        data={
            "sub": existing_user.email,
            "role": existing_user.role
        }
    )

    db.close()

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get("/", response_model=list[UserResponse])
def get_users():

    db: Session = SessionLocal()

    users = db.query(User).all()

    db.close()

    return users