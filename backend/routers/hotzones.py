# backend/routers/hotzones.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from db.session import SessionLocal
from models.hotzone import Hotzone
from schemas.hotzone import HotzoneCreate, HotzoneRead

router = APIRouter(prefix="/hotzones", tags=["hotzones"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=HotzoneRead)
def create_hotzone(payload: HotzoneCreate, db: Session = Depends(get_db)):
    zone = Hotzone(**payload.dict())
    db.add(zone)
    db.commit()
    db.refresh(zone)
    return zone


@router.get("/", response_model=List[HotzoneRead])
def list_hotzones(db: Session = Depends(get_db)):
    return db.query(Hotzone).all()


@router.get("/drawing/{drawing_id}", response_model=List[HotzoneRead])
def list_by_drawing(drawing_id: int, db: Session = Depends(get_db)):
    return db.query(Hotzone).filter(Hotzone.drawing == drawing_id).all()


@router.get("/{hotzone_id}", response_model=HotzoneRead)
def get_hotzone(hotzone_id: int, db: Session = Depends(get_db)):
    zone = db.get(Hotzone, hotzone_id)
    if not zone:
        raise HTTPException(status_code=404, detail="Hotzone not found")
    return zone


@router.put("/{hotzone_id}", response_model=HotzoneRead)
def update_hotzone(hotzone_id: int, payload: HotzoneCreate, db: Session = Depends(get_db)):
    zone = db.get(Hotzone, hotzone_id)
    if not zone:
        raise HTTPException(404, "Hotzone not found")
    for field, value in payload.dict().items():
        setattr(zone, field, value)
    db.commit()
    db.refresh(zone)
    return zone


@router.delete("/{hotzone_id}", status_code=204)
def delete_hotzone(hotzone_id: int, db: Session = Depends(get_db)):
    zone = db.get(Hotzone, hotzone_id)
    if not zone:
        raise HTTPException(404, "Hotzone not found")
    db.delete(zone)
    db.commit()
