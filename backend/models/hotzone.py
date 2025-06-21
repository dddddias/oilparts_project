from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

class Hotzone(Base):
    __tablename__ = "hotzones"
    id        = Column(Integer, primary_key=True, index=True)
    drawing   = Column(Integer, nullable=False)             # ID самой схемы, если их несколько
    part_id   = Column(Integer, ForeignKey("parts.id"), nullable=False)
    x         = Column(Integer, nullable=False)
    y         = Column(Integer, nullable=False)
    width     = Column(Integer, nullable=False)
    height    = Column(Integer, nullable=False)
    number    = Column(Integer, nullable=False)             # цифра, которая будет на картинке

    part      = relationship("Part", backref="hotzones")

from pydantic import BaseModel

class HotzoneBase(BaseModel):
    drawing: int
    part_id: int
    x: int
    y: int
    width: int
    height: int
    number: int

class HotzoneCreate(HotzoneBase):
    pass

class HotzoneRead(HotzoneBase):
    id: int

    class Config:
        orm_mode = True


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from db.session import SessionLocal
from models.hotzone import Hotzone
from schemas.hotzone import HotzoneCreate, HotzoneRead

router = APIRouter(prefix="/hotzones", tags=["hotzones"])

def get_db():
    db = SessionLocal(); 
    try: yield db
    finally: db.close()

@router.post("/", response_model=HotzoneRead)
def create_hotzone(payload: HotzoneCreate, db: Session = Depends(get_db)):
    hz = Hotzone(**payload.dict())
    db.add(hz); db.commit(); db.refresh(hz)
    return hz

@router.get("/", response_model=List[HotzoneRead])
def list_hotzones(db: Session = Depends(get_db)):
    return db.query(Hotzone).all()
