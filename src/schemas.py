from pydantic import BaseModel

class CreateUser(BaseModel):
    username: str
    password: str

class ClassMahasiswa(BaseModel):
    nominal_dana: int
    durasi_hari: int
    nilai_warung: int

class ClassPemberiRekomendasi(BaseModel):
    nama_warung: str
    lokasi_warung: str
    jam_buka_warung: str
    kontak_warung: int
    nama_makanan: str
    harga_makanan: int
    nama_minuman: str
    harga_minuman: int
    
class AuthDetails(BaseModel):
    username: str
    password: str