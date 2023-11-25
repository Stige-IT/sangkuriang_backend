from fastapi import FastAPI
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.middleware.cors import CORSMiddleware

from app.auth.route import auth_router
from app.volunteer.route import volunteer_router
from app.voter.router import voter_router
from core.security import JWTAuth

app = FastAPI(version="0.1.0", title="Sangkuriang API", description="API for Sangkuriang")

# routers
app.include_router(auth_router)
app.include_router(volunteer_router)
app.include_router(voter_router)

# middleware
app.add_middleware(AuthenticationMiddleware, backend=JWTAuth())
# cors middleware
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


@app.get("/")
async def root():
    return {"message": "server is running...🚀"}
