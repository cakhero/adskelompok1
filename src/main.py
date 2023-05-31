from fastapi import FastAPI, Depends, Request, HTTPException, Response, status, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from schemas import CreateUser, Marker
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
def index(request: Request, db: Session = Depends(get_db)):
    context = {"request": request}
    token = request.cookies.get('token')
    if token == None:
        return templates.TemplateResponse("menu.html", context)
    username = crud.verify_user(token)
    if username:
        context['username'] = username
        if crud.get_mahasiswa(db, username):
            return templates.TemplateResponse("landing.html", context)
        if crud.get_pemberi_rekomendasi(db, username):
            warung = crud.read_warung(db)
            context['warung'] = warung
            return templates.TemplateResponse("landingpr.html", context)
        return RedirectResponse("/logout", status_code=status.HTTP_302_FOUND)

    return templates.TemplateResponse("menu.html", context)

@app.post("/register")
async def register(request: Request, db: Session = Depends(get_db)):
    context = {"request": request}
    form = await request.form()
    username = form.get("username")
    password = form.get("password")
    cpassword = form.get("cpassword")
    check = form.get("checkbox")
    print(check)
    if password != cpassword:
        raise HTTPException(status_code=400, detail="Passwords do not match")
        return
    if username == None:
        raise HTTPException(status_code=404, detail="Username Cannot Empty")
        return
    new_user = CreateUser(username=username, password=password)
    
    if check == None:
        crud.create_user(db, new_user)
    else:
        crud.create_pemberi_rekomendasi(db, new_user)
        
    token = crud.login_user(db, username, password)
    response = RedirectResponse("/", status_code=status.HTTP_302_FOUND)
    response.set_cookie("token", token["token"], max_age=24 * 60 * 60)
    return response

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

@app.get("/reset")
async def reset(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("password.html", context)

@app.post("/reset")
async def reset(request: Request, db: Session = Depends(get_db)):
    context = {"request": request}
    token = request.cookies.get("token")
    if token == None:
        return templates.TemplateResponse("menu.html", context)
    form = await request.form()
    old_password = form.get("old_password")
    new_password = form.get("new_password")
    status = crud.change_password(db, token, old_password, new_password)
    print(status)
    if status:
        context['username'] = crud.verify_user(token)
        return templates.TemplateResponse("landing.html", context)
    return templates.TemplateResponse("password.html", context)

@app.get("/report")
async def report(request: Request):
    context = {"request": request}
    return templates.TemplateResponse("report.html", context)

@app.post("/report")
async def report(request: Request, db: Session = Depends(get_db)):
    context = {"request": request}
    token = request.cookies.get("token")
    form = await request.form()
    report = form.get("report")
    if token == None or report == None:
        return RedirectResponse("/", status_code=status.HTTP_302_FOUND)
    report = crud.save_report(db, token, report)
    return RedirectResponse("/", status_code=status.HTTP_302_FOUND)

@app.get("/order")
async def order(request: Request, db: Session = Depends(get_db)):
    context = {"request": request}
    token = request.cookies.get('token')
    context['username'] = crud.verify_user(token)
    uang, hari = crud.get_uang(db, token)
    context['uang'] = uang
    context['hari'] = hari
    return templates.TemplateResponse("order.html", context)

@app.post("/order")
async def order(request: Request, db: Session = Depends(get_db)):
    context = {"request": request}
    token = request.cookies.get("token")
    form = await request.form()
    hari = int(form.get("choices"))
    uang = int(form.get("uang"))
    if token != None:
        status = crud.save_uang(db, token, uang, hari)
    context['uang'] = uang
    context['hari'] = hari
    return templates.TemplateResponse("order.html", context)
    
@app.get("/menu")
async def menu(request: Request):
    context = {"request": request}
    token = request.cookies.get('token')
    context['username'] = crud.verify_user(token)
    return templates.TemplateResponse("detailmenu1.html", context)

@app.get("/sheet")
async def sheet(request: Request, id: int | None = None, db: Session = Depends(get_db)):
    context = {"request": request}
    token = request.cookies.get('token')
    context['username'] = crud.verify_user(token)
    if id:
        warung = crud.get_warung(db, id)
        context["warung"] = warung
    return templates.TemplateResponse("formpr.html", context)

@app.post("/sheet")
async def sheet(request: Request, db: Session = Depends(get_db)):
    context = {"request": request}
    token = request.cookies.get('token')
    form = await request.form()
    nama_item = form.get("nama-makanan")
    deskripsi = form.get("deksripsi")
    harga_item = form.get("harga")
    nama_warung = form.get("nama-warung")
    alamat_warung = form.get("alamat-warung")
    latitude = form.get("latitude")
    longitude = form.get("longitude")
    jam_buka = form.get("jam-buka")
    jam_tutup = form.get("jam-tutup")
    nomor_telepon = form.get("nomor-telepon")
    
    picture = form.get("picture")
    picture_data = picture.file.read()
    target_directory = "/root/adskelompok1/src/web/static/asset/"
    file_location = target_directory+picture.filename
    with open(file_location, "wb+") as file_object:
        file_object.write(picture_data)

    foto = "/static/asset/"+picture.filename
    
    check = crud.save_warung(db, token, nama_item, deskripsi, harga_item, nama_warung,
                              jam_buka, jam_tutup, alamat_warung, nomor_telepon,
                              foto, latitude, longitude)

    if check:
        context['username'] = crud.verify_user(token)
        return RedirectResponse("/", status_code=status.HTTP_302_FOUND)

@app.post("/edit_sheet")
async def edit_sheet(request: Request, db: Session = Depends(get_db)):
    context = {"request": request}
    token = request.cookies.get('token')
    form = await request.form()
    id = form.get("warung_id")
    nama_item = form.get("nama-makanan")
    deskripsi = form.get("deskripsi")
    harga_item = form.get("harga")
    nama_warung = form.get("nama-warung")
    alamat_warung = form.get("alamat-warung")
    latitude = form.get("latitude")
    longitude = form.get("longitude")
    jam_buka = form.get("jam-buka")
    jam_tutup = form.get("jam-tutup")
    nomor_telepon = form.get("nomor-telepon")
    print(id, nama_item, deskripsi, nomor_telepon)
    
    picture = form.get("picture")
    picture_data = picture.file.read()
    target_directory = "/root/adskelompok1/src/web/static/asset/"
    file_location = target_directory+picture.filename
    with open(file_location, "wb+") as file_object:
        file_object.write(picture_data)

    foto = "/static/asset/"+picture.filename
    check = crud.edit_warung(db, id, nama_item, deskripsi, harga_item, nama_warung,
                              jam_buka, jam_tutup, alamat_warung, nomor_telepon,
                              foto, latitude, longitude)
    
    if check:
        context['username'] = crud.verify_user(token)
        return RedirectResponse("/", status_code=status.HTTP_302_FOUND)
    
@app.get("/delete_warung")
async def delete_warung(request: Request, id: int, db: Session = Depends(get_db)):
    context = {"request": request}
    check = crud.delete_warung(db, id)
    token = request.cookies.get('token')
    if check:
        context['username'] = crud.verify_user(token)
        return RedirectResponse("/", status_code=status.HTTP_302_FOUND)
    

# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app, host="0.0.0.0", port=8000)