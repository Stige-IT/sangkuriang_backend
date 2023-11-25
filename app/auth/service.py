from datetime import timedelta

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.auth.response import TokenResponse
from app.volunteer.model import Volunteer
from core.config import get_settings
from core.security import (
    verify_password,
    get_token_payload,
    create_access_token,
    create_refresh_token,
)

settings = get_settings()


# noinspection PyTypeChecker
async def get_token(data, db: Session, is_form=False):
    if is_form:
        user: Volunteer = db.query(Volunteer).filter(Volunteer.nik == str(data.username)).first()
    else:
        user: Volunteer = db.query(Volunteer).filter(Volunteer.nik == str(data.nik)).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="Email is not registered with us.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not verify_password(data.password, user.password):
        raise HTTPException(
            status_code=401,
            detail="Invalid Login Credentials.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return await _get_user_token(user)


async def get_refresh_token(token, db):
    payload = get_token_payload(token=token)
    user_id = payload.get("id", None)
    if not user_id:
        raise HTTPException(
            status_code=401,
            detail="Invalid refresh token.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = db.query(Volunteer).filter(Volunteer.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid refresh token.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return await _get_user_token(user=user, refresh_token=token)


async def _get_user_token(user, refresh_token=None):
    payload = {"id": user.id}

    access_token_expiry = timedelta(hours=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = await create_access_token(payload, access_token_expiry)
    if not refresh_token:
        refresh_token = await create_refresh_token(payload)
    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token,
        expires_in=access_token_expiry.seconds,
        role=user.role,
    )
