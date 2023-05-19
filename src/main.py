from fastapi import FastAPI, Depends
from .schemas import CreateUser
from sqlalchemy.orm import Session
from .database import get_db
from .models import User

app = FastAPI()

@app.post("/")
def create(details: CreateUser, db : Session = Depends(get_db)):
        to_create = User(
            username=details.username,
            password=details.password,
            reportBug=details.reportBug
        )
        db.add(to_create)
        db.commit()
        return{
            "success": True,
            "created_id": to_create.id
        }
    
@app.get("/")
def get_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(User).filter(User.id==id).first()

@app.delete("/")
def delete(id: int, db:Session=Depends(get_db)):
    return db.query(User).filter(User.id==id).delete()
    db.commit()
    return {"success": True}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)