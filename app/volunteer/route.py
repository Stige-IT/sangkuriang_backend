from typing import Annotated

from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.volunteer.model import Volunteer
from core.database import get_db
from core.security import oauth2_scheme

volunteer_router = APIRouter(
    prefix="/volunteer",
    tags=["volunteer"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(oauth2_scheme)],
)


# get volunteer
@volunteer_router.get("/")
async def get_volunteer(db: Session = Depends(get_db)):
    volunteer = db.query(Volunteer).filter(Volunteer.role != 'admin').all()
    return volunteer


# add volunteer
@volunteer_router.post("/")
async def add_volunteer():
    return {"message": "success add volunteer"}


# upload file volunteer
@volunteer_router.post("/upload")
async def upload_file(
        file: Annotated[bytes, UploadFile],
):
    return {"message": "success upload file volunteer",
            "data": {
                "file" : file.filename
                }
            }
