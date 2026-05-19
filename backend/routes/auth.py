from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import SessionLocal
import models
import secrets
from schemas.user import UserCreate
from core.security import hash_password, verify_password, create_access_token
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from backend.core.email import send_verification_email
from backend.core.limiter import limiter
from backend.core.analytics import track_event
from fastapi import Request

router = APIRouter(prefix="/auth", tags=["Auth"])

SECRET_KEY = "your_super_secret_key"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


# ==============================
# DB
# ==============================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ==============================
# REGISTER
# ==============================
@router.post("/register")
@limiter.limit("5/minute")
def register(user: UserCreate, db: Session = Depends(get_db)):
    
    hashed_pw = hash_password(user.password)

    verification_token = secrets.token_urlsafe(32)

    db_user = models.User(
        username=user.username,
        email=user.email,
        password=hashed_pw,
        verification_token=verification_token
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    verification_link = (
    f"http://localhost:3000/verify-email/"
    f"{verification_token}"
    )

    send_verification_email(
        new_user.email,
        verification_link
    )

    return db_user


# ==============================
# GET USERS
# ==============================
@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()    


# ==============================
# LOGIN
# ==============================
@router.post("/login")
@limiter.limit("10/minute")
def login(email: str, password: str, db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.email == email).first()

    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    track_event(
        db,
        user.id,
        "login"
    )

    token = create_access_token({"user_id": user.id})

    return {"access_token": token}


# ==============================
# GET CURRENT USER
# ==============================
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")

        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        return user_id

    except JWTError:
        raise HTTPException(status_code=401, detail="Token invalid or expired")


# ==============================
# TEST PROTECTED ROUTE
# ==============================
@router.get("/protected")
def protected(user = Depends(get_current_user)):
    return {"user_id": user}     

@router.get("/verify-email/{token}")
def verify_email(token: str, db: Session = Depends(get_db)):

    user = db.query(models.User).filter(
        models.User.verification_token == token
    ).first()

    if not user:
        raise HTTPException(
            status_code=400,
            detail="Invalid token"
        )

    user.is_verified = True
    user.verification_token = None

    db.commit()

    return {
        "message": "Email verified"
    }

