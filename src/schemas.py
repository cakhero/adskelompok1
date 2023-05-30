from pydantic import BaseModel

class CreateUser(BaseModel):
    username: str
    password: str

class ClassMahasiswa(BaseModel):
    nominal_dana: int
    durasi_hari: int
    nilai_warung: int

class Warung(BaseModel):
    nama_item: str
    deskripsi: str
    harga_item: int
    nama_warung: str
    lokasi_warung: str
    jam_buka_warung: str
    jam_tutup_warung: str
    alamat_warung: str
    kontak_warung: str
    foto_warung: str
    latitude: str
    longitude: str
    
class AuthDetails(BaseModel):
    username: str
    password: str