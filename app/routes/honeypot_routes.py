from fastapi import APIRouter
from app import schemas 
from typing import List
from app import schemas
from fastapi import Depends
from app.database import get_db 
from sqlalchemy.orm import Session
from app import models
from app.database import SessionLocal

router = APIRouter()
@router.post("/honeypot", response_model=schemas.HoneypotEventResponse)
def log_honeypot_event(event: schemas.HoneypotEventCreate, db: Session = Depends(get_db)):
    db_event = models.HoneypotEvent(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

@router.get("/honeypot", response_model=List[schemas.HoneypotEventResponse])
def get_honeypot_events(db: Session = Depends(get_db)):
    return db.query(models.HoneypotEvent).all()

@router.post("/honeypot", response_model=schemas.HoneypotEventResponse)
def create_honeypot_event():
    pass  