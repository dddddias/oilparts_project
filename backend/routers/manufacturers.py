# routers/manufacturers.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from db.session import SessionLocal
from models.manufacturer import Manufacturer
from schemas.manufacturer import ManufacturerCreate, ManufacturerRead

router = APIRouter(prefix="/manufacturers", tags=["manufacturers"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ManufacturerRead)
def create_manufacturer(payload: ManufacturerCreate, db: Session = Depends(get_db)):
    m = Manufacturer(**payload.dict())
    db.add(m)
    db.commit()
    db.refresh(m)
    return m

@router.get("/", response_model=List[ManufacturerRead])
def list_manufacturers(db: Session = Depends(get_db)):
    return db.query(Manufacturer).all()

@router.get("/{manu_id}", response_model=ManufacturerRead)
def get_manufacturer(manu_id: int, db: Session = Depends(get_db)):
    m = db.get(Manufacturer, manu_id)
    if not m:
        raise HTTPException(404, "Manufacturer not found")
    return m

@router.put("/{manu_id}", response_model=ManufacturerRead)
def update_manufacturer(manu_id: int, payload: ManufacturerCreate, db: Session = Depends(get_db)):
    m = db.get(Manufacturer, manu_id)
    if not m:
        raise HTTPException(404, "Manufacturer not found")
    for field, val in payload.dict().items():
        setattr(m, field, val)
    db.commit()
    db.refresh(m)
    return m

@router.delete("/{manu_id}", status_code=204)
def delete_manufacturer(manu_id: int, db: Session = Depends(get_db)):
    m = db.get(Manufacturer, manu_id)
    if not m:
        raise HTTPException(404, "Manufacturer not found")
    db.delete(m)
    db.commit()
