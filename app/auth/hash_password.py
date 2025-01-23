import bcrypt
from typing import Union


def hash_password(plain_password: Union[str, bytes]) -> bytes:
    """
    Takes a plain password as input and returns a hashed password.
    
    :param plain_password: The plain text password to hash.
    :return: The hashed password.
    """
    # Ensure the password is in bytes
    if isinstance(plain_password, str):
        plain_password = plain_password.encode('utf-8')
    
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(plain_password, salt)
    return hashed_password
