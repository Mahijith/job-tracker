from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.models.job import StatusEnum

class JobCreate(BaseModel):
    company: str
    role: str
    location: Optional[str] = None
    status: StatusEnum = StatusEnum.applied
    notes: Optional[str] = None

class JobUpdate(BaseModel):
    company: Optional[str] = None
    role: Optional[str] = None
    location: Optional[str] = None
    status: Optional[StatusEnum] = None
    notes: Optional[str] = None

class JobResponse(BaseModel):
    id: int
    company: str
    role: str
    location: Optional[str]
    status: StatusEnum
    notes: Optional[str]
    applied_at: datetime

    model_config = {"from_attributes": True}