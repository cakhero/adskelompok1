from fastapi import FastAPI, Depends, Request, HTTPException, Response, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from schemas import CreateUser
from core.crud import crud
from sqlalchemy.orm import Session
from database import get_db
from models import User
from core.crud import crud
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="web")

app.mount("/static", StaticFiles(directory="web/static"), name="static")
    
@app.get("/")
def index(request: Request):
    context = {"request": request}
    token = request.cookies.get('token')
    if token == None:
        return templates.TemplateResponse("menu.html", context)
    if crud.verify_user(token):
        return templates.TemplateResponse("landing.html", context)
    return templates.TemplateResponse("menu.html", context)

@app.post("/register")
async def register(request: Request, db: Session = Depends(get_db)):
    context = {"request": request}
    form = await request.form()
    username = form.get("username")
    password = form.get("password")
    cpassword = form.get("cpassword")
    if password != cpassword:
        raise HTTPException(status_code=400, detail="Passwords do not match")
        return
    new_user = CreateUser(username=username, password=password)
    crud.create_user(db, new_user)
    return templates.TemplateResponse("landing.html", context)

@app.post("/login")
async def login(request: Request, db: Session = Depends(get_db)):
    context = {"request": request}
    form = await request.form()
    username = form.get("username")
    password = form.get("password")
    token = crud.login_user(db, username, password)
    response = RedirectResponse("/", status_code=status.HTTP_302_FOUND)
    response.set_cookie("token", token["token"], max_age=24 * 60 * 60)
    return response
    
@app.get("/logout")
async def logout(request: Request):
    token = request.cookies.get("token")
    response = RedirectResponse("/", status_code=status.HTTP_302_FOUND)
    response.delete_cookie("token")
    return response

# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app, host="0.0.0.0", port=8000)