from fastapi import APIRouter, Depends, HTTPException, status
from app.core.deps import admin_only
from app.core.exceptions import EmailExists, UserExists
from app.services.user import add_user as add_user_svc
from app.schemas.user import UserAdd


router = APIRouter()

@router.post("/add")
async def add_user(user_data: UserAdd, access = Depends(admin_only)):
    try:
        new_user = await add_user_svc(user_data=user_data)
    except UserExists:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "User already exists")
    except EmailExists:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "User with that email already exists")
        
    return new_user
