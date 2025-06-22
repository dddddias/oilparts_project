from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from backend.db.session import SessionLocal
from models.unit_type import UnitType

router = APIRouter(prefix="/unit_types", tags=["unit_types"])

# зависимость для получения сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=dict)
def create_unit_type(payload: dict, db: Session = Depends(get_db)):
    ut = UnitType(**payload)
    db.add(ut)
    db.commit()
    db.refresh(ut)
    return {"id": ut.id, "name": ut.name, "description": ut.description}

@router.get("/", response_model=List[dict])
def list_unit_types(db: Session = Depends(get_db)):
    return [{"id": u.id, "name": u.name, "description": u.description} for u in db.query(UnitType).all()]

@router.get("/{unit_type_id}", response_model=dict)
def get_unit_type(unit_type_id: int, db: Session = Depends(get_db)):
    ut = db.get(UnitType, unit_type_id)
    if not ut:
        raise HTTPException(404, "Not found")
    return {"id": ut.id, "name": ut.name, "description": ut.description}

@router.put("/{unit_type_id}", response_model=dict)
def update_unit_type(unit_type_id: int, payload: dict, db: Session = Depends(get_db)):
    ut = db.get(UnitType, unit_type_id)
    if not ut:
        raise HTTPException(404, "Not found")
    for k,v in payload.items():
        setattr(ut, k, v)
    db.commit()
    db.refresh(ut)
    return {"id": ut.id, "name": ut.name, "description": ut.description}

@router.delete("/{unit_type_id}", status_code=204)
def delete_unit_type(unit_type_id: int, db: Session = Depends(get_db)):
    ut = db.get(UnitType, unit_type_id)
    if not ut:
        raise HTTPException(404, "Not found")
    db.delete(ut)
    db.commit()
