from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.user import User
from auth.jwt_handler import create_token
from auth.auth_bearer import JWTBearer
from auth.utils import get_current_user
from fastapi import Depends
from schemas.user import UserAuth

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(data: UserAuth, db: Session = Depends(get_db)):
    user = User(username=data.username, password=data.password)
    db.add(user)
    db.commit()
    db.refresh(user)

    return {"message": "User created"}

@router.post("/login")
def login(data: UserAuth, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == data.username).first()

    if not user or user.password != data.password:
        raise HTTPException(status_code=401, detail="Invalid login")

    token = create_token({"sub": user.username})

    return {
        "access_token": token,
        "token_type": "bearer"
    }