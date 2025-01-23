import os
import jwt
from datetime import datetime, timedelta
from typing import Dict

def generate_token(user_info: Dict[str, str]) -> str:
    """
    Generates a JWT token for authentication.

    :param user_info: A dictionary containing user information.
    :return: A JWT token as a string.
    """
    secret_key = os.environ["JWT_SECRET_KEY"]
    algorithm = "HS256"
    expiration_time = datetime.utcnow() + timedelta(hours=1)

    payload = {
        "user_id": user_info["user_id"],
        "username": user_info["username"],
        "exp": expiration_time
    }

    token = jwt.encode(payload, secret_key, algorithm=algorithm)
    return token
