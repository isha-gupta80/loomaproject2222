from fastapi import APIRouter, Depends
from app.api.routes import auth, schools
from app.core.deps import get_current_session


api_router = APIRouter()
api_router.include_router(schools.router, prefix="/schools", dependencies=[Depends(get_current_session)], tags=["schools"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
