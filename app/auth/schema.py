from pydantic import BaseModel


class LoginRequest(BaseModel):
    nik: str
    password: str

