from sqlalchemy.orm import session
from fastapi import HTTPException
import schemas
import models
from core.auth import auth_handler

class Crud():
    def create_user(self, db: session, new_user:schemas.CreateUser):
        hashed_password = auth_handler.get_password_hash(new_user.password)
        user = models.User(username=new_user.username, password=hashed_password)
        db.add(user)
        db.commit()

    def get_user(self, db: session, username: str):
        user = db.query(models.User).filter(models.User.username == username).first()
        return user
    
    
    def login_user(self, db: session, username: str, password: str):
        user = self.get_user(db, username)
        # print(user)
        # print(user.password)
        # print(auth_handler.get_password_hash(password))
        # print(auth_handler.verify_password(user.password, auth_handler.get_password_hash(password)))
        if (user is None) or (not auth_handler.verify_password(password, user.password)):
            raise HTTPException(status_code=401, detail='Invalid username and/or password')
        token = auth_handler.encode_token(user.username)
        return { 'token': token }
    
    def verify_user(self, token: str):
        user = auth_handler.decode_token(token)
        return user
    
crud = Crud()