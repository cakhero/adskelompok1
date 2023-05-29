from sqlalchemy.orm import session
from fastapi import HTTPException
import schemas
import models
from core.auth import auth_handler

class Crud():
    def create_user(self, db: session, new_user:schemas.CreateUser):
        hashed_password = auth_handler.get_password_hash(new_user.password)
        user = models.Mahasiswa(username=new_user.username, password=hashed_password)
        db.add(user)
        db.commit()
        db.refresh(user)
    
    def get_user(self, db: session, username: str):
        user = db.query(models.User).filter(models.User.username == username).first()
        return user
     
    def get_mahasiswa(self, db:session, username: str) -> models.Mahasiswa:
        user = self.get_user(db, username)
        mahasiswa = db.query(models.Mahasiswa).filter(models.Mahasiswa.user_id == user.id).first()
        return mahasiswa

    def login_user(self, db: session, username: str, password: str):
        user = self.get_user(db, username)
        if (user is None) or (not auth_handler.verify_password(password, user.password)):
            raise HTTPException(status_code=401, detail='Invalid username and/or password')
        token = auth_handler.encode_token(user.username)
        return { 'token': token }
    
    def verify_user(self, token: str):
        user = auth_handler.decode_token(token)
        return user
    
    def change_password(self, db: session, token: str, old_password: str, new_password: str):
        user = self.verify_user(token)
        user = self.get_user(db, user)
        if auth_handler.verify_password(old_password, user.password):
            new_password = auth_handler.get_password_hash(new_password)
            user.password = new_password
            db.commit()
            db.refresh(user)
            return True
        return False 
    
    def save_report(self, db: session, token: str, report: str):
        user = self.verify_user(token)
        user = self.get_user(db, user)
        user.report_bug = report
        db.commit()
        db.refresh(user)
        return True
        
    def save_uang(self, db: session, token: str, uang : int, hari: int):
        user = self.verify_user(token)
        user = self.get_mahasiswa(db, user)
        user.nominal_dana = uang
        user.durasi_hari = hari
        db.commit()
        db.refresh(user)
        return True
        
        
    
crud = Crud()