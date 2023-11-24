from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session

from app.voter.model import Voter
from core.database import get_db

voter_router = APIRouter(
    prefix="/voter",
    tags=["voter"],
    responses={404: {"description": "Not found"}},
)


@voter_router.get("/")
async def get(request: Request, db: Session = Depends(get_db)):
    voter = db.query(Voter).filter(Voter.id == request.state.user.id).all()
    return {
        "message": "success get voter",
        "data": voter
    }



@voter_router.post("/")
async def create(request: VoterRequest, db: Session = Depends(get_db)):
    voter = db.query(Voter).filter(Voter.id == request.state.user.id).first()
    if voter:
        return {
            "message": "voter already exist"
        }
    else:
        voter = db.query(Voter).filter(Voter.id == request.state.user.id).first()
        return {
            "message": "success create voter",
            "data": voter
        }