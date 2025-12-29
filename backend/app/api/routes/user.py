from beanie import PydanticObjectId
from fastapi import APIRouter, Depends, HTTPException, status
from app.core.deps import admin_only
from app.core.exceptions import EmailExists, UserExists, UserNotFound
from app.services.user import add_user as add_user_svc, delete_user_by_id
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

@router.delete("/{user_id}", status_code=204)
async def delete_user(user_id: PydanticObjectId , access = Depends(admin_only)):
    try:
        await delete_user_by_id(user_id)
    except UserNotFound:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "User not found")
