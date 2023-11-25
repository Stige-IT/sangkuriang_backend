from typing import Optional

from pydantic import BaseModel


class VoterRequest(BaseModel):
    id_volunteer: str
    nkk: Optional[str] = None
    nik: Optional[str] = None
    name: Optional[str] = None
    birth_date: Optional[str] = None
    place_of_birth: Optional[str] = None
    gender: Optional[str] = None
    phone_number: Optional[str] = None
    province: Optional[str] = None
    regency: Optional[str] = None
    district: Optional[str] = None
    rt: Optional[str] = None
    rw: Optional[str] = None
    address: Optional[str] = None
    role: Optional[str] = None
