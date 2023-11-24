from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.schema import LoginRequest
from app.auth.service import get_token
from core.database import get_db

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@auth_router.post("/login")
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    return await get_token(request, db)


