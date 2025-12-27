from beanie import PydanticObjectId
from pydantic import EmailStr

from app.models.user import UserDoc


async def get_user_by_email(email: EmailStr) -> UserDoc | None:
    user = await UserDoc.find_one(UserDoc.email == email)
    if not user:
        return None
    return user

async def get_user_by_username(username: str) -> UserDoc | None:
    user = await UserDoc.find_one(UserDoc.username == username)
    if not user:
        return None
    return user

async def get_user_by_id(id: PydanticObjectId) -> UserDoc | None:
    user = await UserDoc.find_one(UserDoc.id == id)
    if not user:
        return None
    return user
