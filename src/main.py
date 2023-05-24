from fastapi import FastAPI, Depends, Request
from fastapi.staticfiles import StaticFiles
from schemas import CreateUser
from core.crud import create_user
from sqlalchemy.orm import Session
from database import get_db
from models import User
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="web")

app.mount("/static", StaticFiles(directory="web/static"), name="static")

# @app.post("/")
# def create(details: CreateUser, db : Session = Depends(get_db)):
#         to_create = User(
#             username=details.username,
#             password=details.password,
#             report_bug=details.report_bug
#         )
#         db.add(to_create)
#         db.commit()
#         return{
#             "success": True,
#             "created_id": to_create.id
#         }
    
@app.get("/")
def index(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("menu.html", context)

@app.post("/register")
async def register(request: Request, db: Session = Depends(get_db)):
    context = {"request": request}
    form = await request.form()
    username = form.get("username")
    password = form.get("password")
    cpassword = form.get("cpassword")
    new_user = CreateUser(username=username, password=password)
    create_user(db, new_user)
    return {"status": "OK"}

@app.post("/login")
async def register(request: Request, db: Session = Depends(get_db)):
    context = {"request": request}
    form = await request.form()
    username = form.get("username")
    password = form.get("password")
    #print(username, password)
    return {"status": "OK"}
    

# @app.delete("/")
# def delete(id: int, db:Session=Depends(get_db)):
#     return db.query(User).filter(User.id==id).delete()
#     db.commit()
#     return {"success": True}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)