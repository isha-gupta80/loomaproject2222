from enum import Enum
from typing import List
from beanie import PydanticObjectId
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class SchoolStatus(str, Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    MAINTENANCE = "maintenance"

class Contact(BaseModel):
    email: EmailStr
    phone: str
    headmaster: str

class LoomaInfo(BaseModel):
    id: str
    serialNumber: str
    version: str
    lastUpdate: datetime

class ContactUpdate(BaseModel):
    email: EmailStr | None = None
    phone: str | None = None
    headmaster: str | None = None

class LoomaInfoUpdate(BaseModel):
    id: str | None = None
    serialNumber: str | None = None
    version: str | None = None
    lastUpdate: datetime | None = None

class SchoolOut(BaseModel):
    id: PydanticObjectId
    name: str
    latitude: float
    longitude: float
    contact: Contact
    province: str
    district: str
    palika: str
    status: SchoolStatus
    lastSeen: datetime
    loomaId: str
    loomaCount: int
    looma: LoomaInfo
    # createdAt: datetime
    # updatedAt: datetime
    qrScans: List[str] | None = []
    accessLogs: List[str] | None = []

class SchoolCreate(BaseModel):
    name: str
    latitude: float
    longitude: float
    contact: Contact
    province: str
    district: str
    palika: str
    status: SchoolStatus
    lastSeen: datetime
    loomaId: str
    loomaCount: int
    looma: LoomaInfo

class SchoolUpdate(BaseModel):
    name: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    contact: ContactUpdate | None = None
    province: str | None = None
    district: str | None = None
    palika: str | None = None
    status: SchoolStatus | None = None
    lastSeen: datetime | None = None
    loomaId: str | None = None
    loomaCount: int | None = None
    looma: LoomaInfoUpdate | None = None

class SchoolUpdateStatus(BaseModel):
    status: SchoolStatus
