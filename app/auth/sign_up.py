from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.auth.hash_password import hash_password
from app.modassembly.database.sql.get_sql_session import get_sql_session
from app.models.User import User

router = APIRouter()

class SignUpData(BaseModel):
    username: str
    email: str
    password: str

class SignUpResponse(BaseModel):
    message: str

@router.post("/sign-up", response_model=SignUpResponse)
def sign_up(user_data: SignUpData, db: Session = Depends(get_sql_session)) -> SignUpResponse:
    """
    Endpoint for user sign-up.
    
    1) Receives user sign-up data.
    2) Hashes the password.
    3) Stores user data in the database.
    4) Returns a success message.
    """
    # Check if the username or email already exists
    existing_user = db.query(User).filter(
        (User.username == user_data.username) | (User.email == user_data.email)
    ).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username or email already exists.")

    # Hash the password
    hashed_password = hash_password(user_data.password)

    # Create a new user instance
    new_user = User(
        username=user_data.username,
        email=user_data.email,
        password_hash=hashed_password.decode('utf-8')
    )

    # Add the new user to the database
    db.add(new_user)
    db.commit()

    return SignUpResponse(message="User successfully signed up.")
