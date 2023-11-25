from pydantic import BaseModel


class LoginRequest(BaseModel):
    nik: str = None
    password: str = None

