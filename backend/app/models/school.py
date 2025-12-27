from beanie import Document
from pydantic import BaseModel, EmailStr
from datetime import datetime

from pymongo import IndexModel

class Contact(BaseModel):
    email: EmailStr
    phone: str
    headmaster: str

class LoomaInfo(BaseModel):
    id: str
    serialNumber: str
    version: str
    lastUpdate: datetime

class School(Document):
    name: str
    latitude: float
    longitude: float
    contact: Contact
    province: str
    district: str
    palika: str
    status: str
    lastSeen: datetime
    loomaId: str
    loomaCount: int
    looma: LoomaInfo
    createdAt: datetime
    updatedAt: datetime

    class Settings:
        name = "schools"
        indexes = [
            IndexModel([
                ("name", "text"),
                ("province", "text"),
                ("district", "text"),
                ("palika", "text")
            ])
        ]

