from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.auth.verify_password import verify_password
from app.auth.generate_token import generate_token
from app.modassembly.database.sql.get_sql_session import get_sql_session
from app.models.User import User

router = APIRouter()

class LoginData(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

@router.post("/login", response_model=TokenResponse, summary="User Login", description="Verifies user credentials and returns a JWT token.")
def login(login_data: LoginData, db: Session = Depends(get_sql_session)) -> TokenResponse:
    user = db.query(User).filter(User.username == login_data.username).first()
    if not user or not verify_password(login_data.password, user.password_hash.__str__()):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = generate_token({"user_id": user.id.__str__(), "username": user.username.__str__()})
    return TokenResponse(access_token=token)
