from sqlalchemy.orm import session
from fastapi import HTTPException
import schemas
import models
from auth import AuthHandler

def create_user(db: session, new_user:schemas.CreateUser):
    hashed_password = AuthHandler.get_password_hash(new_user.password)
    user = models.User(username=new_user.username, password=hashed_password)
    db.add(user)
    db.commit()

def get_user(db: session, username: str):
    user = db.query(models.User).filter(models.User.username == username).first()
    return user
    
def login_user(db: session, username: str, password: str):
    user = get_user(db, username)
    if (user is None) or (not AuthHandler.verify_password(AuthHandler.password, user['password'])):
        raise HTTPException(status_code=401, detail='Invalid username and/or password')
    token = AuthHandler.encode_token(user['username'])
    return { 'token': token }