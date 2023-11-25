import datetime

from sqlalchemy import Column, String, ForeignKey, DATETIME

from core.database import Base


class Voter(Base):
    __tablename__ = "voter"
    id = Column(String(100), primary_key=True, autoincrement=False)
    id_volunteer = Column(String(100), ForeignKey('volunteer.id'), nullable=False)
    nkk = Column(String(100), nullable=True)
    nik = Column(String(100), nullable=True)
    password = Column(String(100), nullable=True)
    name = Column(String(100), nullable=True)
    birth_date = Column(String(100), nullable=True)
    place_of_birth = Column(String(100), nullable=True)
    gender = Column(String(100), nullable=True)
    phone_number = Column(String(100), nullable=True)
    province = Column(String(100), nullable=True)
    regency = Column(String(100), nullable=True)
    district = Column(String(100), nullable=True)
    village = Column(String(100), nullable=True)
    rt = Column(String(100), nullable=True)
    rw = Column(String(100), nullable=True)
    address = Column(String(100), nullable=True)
    role = Column(String(100), nullable=True, default="user")
    ktp = Column(String(100), nullable=True)
    created_at = Column(DATETIME, nullable=True, default=datetime.datetime.now())