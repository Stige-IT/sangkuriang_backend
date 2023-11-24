from pydantic import BaseModel


class VoterRequest(BaseModel):
    nkk: str
    nik: str
    name: str
    birth_date: str
    place_of_birth: str
    gender: str
    phone_number: str
    province: str
    regency: str
    district: str
    rt: str
    rw: str
    address: str
    role: str
