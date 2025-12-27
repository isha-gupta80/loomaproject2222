from beanie import PydanticObjectId
from pydantic import BaseModel, EmailStr

from app.models.user import Role


class UserOut(BaseModel):
    id: PydanticObjectId
    username: str
    email: EmailStr
    role: Role
