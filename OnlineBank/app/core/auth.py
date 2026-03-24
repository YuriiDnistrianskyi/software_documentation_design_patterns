from fastapi import HTTPException, status
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone

from app.core.config import SECRET_KEY

def create_access_token(user_id: int, email: str):
    encode = {
        'user_id': user_id,
        'email': email,
    }
    expire = datetime.now(timezone.utc) + timedelta(minutes=10)
    encode.update({'exp': expire})
    return jwt.encode(encode, SECRET_KEY, algorithm='HS256')

def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Signature expired. Please log in again.'
        )
