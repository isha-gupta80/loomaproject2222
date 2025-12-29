from datetime import datetime, timezone
from beanie import PydanticObjectId
from pydantic import EmailStr

from app.core.exceptions import EmailExists, UserExists, UserNotFound
from app.core.security import get_password_hash
from app.models.user import UserDoc
from app.schemas.user import UserAdd


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

async def get_user_by_id(user_id: PydanticObjectId) -> UserDoc | None:
    user = await UserDoc.find_one(UserDoc.id == user_id)
    if not user:
        return None
    return user

async def add_user(user_data: UserAdd) -> UserDoc:
    hashed_password = get_password_hash(user_data.password)

    if await get_user_by_username(user_data.username) is not None:
        raise UserExists()

    if await get_user_by_email(user_data.email) is not None:
        raise EmailExists()

    new_user = UserDoc(
        username=user_data.username,
        email=user_data.email,
        passwordHash=hashed_password,
        role=user_data.role,
        createdAt=datetime.now(timezone.utc),
    )
    await UserDoc.create(new_user)
    return new_user

async def delete_user_by_id(user_id: PydanticObjectId):
    user_to_delete = await UserDoc.find_one(UserDoc.id == user_id)
    if not user_to_delete:
        raise UserNotFound
    await user_to_delete.delete()
