from pydantic import BaseModel

class CreateUser(BaseModel):
    username: str
    password: str
    reportBug : str

class ClassMahasiswa(BaseModel):
    nominalDana: int
    durasiHari: int
    nilaiWarung: int


class ClassPemberiRekomendasi(BaseModel):
    namaWarung: str
    lokasiWarung: str
    jamBukaWarung: str
    kontakWarung: int
    namaMakanan: str
    hargaMakanan: int
    namaMinuman: str
    hargaMinuman: int