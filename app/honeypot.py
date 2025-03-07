from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas
from app.schemas import SomeSchema  


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/honeypot", response_model=schemas.HoneypotEventResponse)
def log_honeypot_event(event: schemas.HoneypotEventCreate, db: Session = Depends(get_db)):
    db_event = models.HoneypotEvent(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event