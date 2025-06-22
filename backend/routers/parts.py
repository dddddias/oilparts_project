# routers/parts.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from backend.db.session import SessionLocal
from models.part import Part
from schemas.part import PartCreate, PartRead

router = APIRouter(prefix="/parts", tags=["parts"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=PartRead)
def create_part(payload: PartCreate, db: Session = Depends(get_db)):
    # опционально: проверить, что manufacturer и node существуют
    part = Part(**payload.dict())
    db.add(part)
    db.commit()
    db.refresh(part)
    return part

@router.get("/", response_model=List[PartRead])
def list_parts(db: Session = Depends(get_db)):
    return db.query(Part).all()

@router.get("/{part_id}", response_model=PartRead)
def get_part(part_id: int, db: Session = Depends(get_db)):
    part = db.get(Part, part_id)
    if not part:
        raise HTTPException(404, "Part not found")
    return part

@router.put("/{part_id}", response_model=PartRead)
def update_part(part_id: int, payload: PartCreate, db: Session = Depends(get_db)):
    part = db.get(Part, part_id)
    if not part:
        raise HTTPException(404, "Part not found")
    for field, val in payload.dict().items():
        setattr(part, field, val)
    db.commit()
    db.refresh(part)
    return part

@router.delete("/{part_id}", status_code=204)
def delete_part(part_id: int, db: Session = Depends(get_db)):
    part = db.get(Part, part_id)
    if not part:
        raise HTTPException(404, "Part not found")
    db.delete(part)
    db.commit()
