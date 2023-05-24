from sqlalchemy import Integer, String, Text, ForeignKey
from sqlalchemy.sql.schema import Column
from database import Base

class User(Base):
    __tablename__ = 'akun'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    report_bug = Column(Text)

class Mahasiswa(User):
    __tablename__ = 'mahasiswa'
    user_id = Column(Integer, ForeignKey('akun.id'), primary_key=True)
    nominal_dana = Column(Integer)
    durasi_hari = Column(Integer)
    nilai_warung = Column(Integer)

class PemberiRekomendasi(User):
    __tablename__ = 'pemberi_rekomendasi'
    user_id = Column(Integer, ForeignKey('akun.id'), primary_key=True)
    nama_warung = Column(String)
    lokasi_warung = Column(String)
    jam_buka_warung = Column(String)
    kontak_warung = Column(Integer)
    nama_makanan = Column(String)
    harga_makanan = Column(Integer)
    nama_minuman = Column(String)
    harga_minuman = Column(Integer)