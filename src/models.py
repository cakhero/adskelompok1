from sqlalchemy import Integer, String, Text, ForeignKey, Time
from sqlalchemy.sql.schema import Column
from database import Base

class User(Base):
    __tablename__ = 'akun'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    
class report(Base):
    __tablename__ = 'report_bug'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    report = Column(Text)

class Mahasiswa(User):
    __tablename__ = 'mahasiswa'
    user_id = Column(Integer, ForeignKey('akun.id'), primary_key=True)
    nominal_dana = Column(Integer)
    durasi_hari = Column(Integer)
    nilai_warung = Column(Integer)

class PemberiRekomendasi(User):
    __tablename__ = 'pemberi_rekomendasi'
    user_id = Column(Integer, ForeignKey('akun.id'), primary_key=True)
    
class Warung(Base):
    __tablename__ = 'warung'
    id = Column(Integer, primary_key=True)
    nama_item = Column(String)
    deskripsi = Column(Text)
    harga_item = Column(Integer)
    nama_warung = Column(String)
    lokasi_warung = Column(String)
    jam_buka_warung = Column(Time)
    jam_tutup_warung = Column(Time)
    alamat_warung = Column(String)
    kontak_warung = Column(String)
    foto_warung = Column(String)
    latitude = Column(String)
    longitude = Column(String)
    