from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True

class HoneypotEventCreate(BaseModel):
    attacker_ip: str
    attack_type: str

class HoneypotEventResponse(HoneypotEventCreate):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True