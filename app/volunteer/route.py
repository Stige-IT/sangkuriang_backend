from fastapi import APIRouter

volunteer_router = APIRouter(
    prefix="/volunteer",
    tags=["volunteer"],
    responses={404: {"description": "Not found"}},
)



