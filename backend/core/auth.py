from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "secret"
ALGORITHM = "HS256"

def create_access_token(data: dict):

    to_encode = data.copy()

    access_token_expires = timedelta(days=7)

    expire = datetime.utcnow() + access_token_expires

    to_encode.update({
        "exp": expire
    })

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt 