from jose import jwt
from database import SessionLocal
from models.user import User

SECRET_KEY = "secret"
ALGORITHM = "HS256"

def get_current_user(token: str):
    db = SessionLocal()
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username = payload.get("sub")

    user = db.query(User).filter(User.username == username).first()
    db.close()

    return user