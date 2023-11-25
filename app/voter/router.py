import uuid

from fastapi import APIRouter, Request, Depends, HTTPException
from sqlalchemy.orm import Session

from app.voter.model import Voter
from app.voter.schema import VoterRequest
from core.database import get_db
from core.security import oauth2_scheme

voter_router = APIRouter(
    prefix="/voter",
    tags=["voter"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(oauth2_scheme)],
)


@voter_router.get("")
async def get(db: Session = Depends(get_db)):
    voter = db.query(Voter).all()
    return {"data": voter}


@voter_router.get("/me")
async def get_voter(request: Request, db: Session = Depends(get_db)):
    voter = db.query(Voter).filter(Voter.id_volunteer == request.user.id).all()
    return {"data": voter}


@voter_router.post("")
async def create(request: VoterRequest, db: Session = Depends(get_db)):
    voter = db.query(Voter).filter(Voter.nik == request.nik).first()
    if not voter:
        voter = Voter(
            id=str(uuid.uuid4()),
            id_volunteer=request.id_volunteer,
            nik=request.nik,
            name=request.name,
            address=request.address,
        )
        db.add(voter)
        db.commit()
        db.refresh(voter)
        return {"data": voter}

    raise HTTPException(status_code=400, detail="NIK already registered")
