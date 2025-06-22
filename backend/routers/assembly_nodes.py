from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from backend.db.session import SessionLocal
from models.assembly_node import AssemblyNode
from schemas.assembly_node import AssemblyNodeCreate, AssemblyNodeRead

router = APIRouter(prefix="/assembly_nodes", tags=["assembly_nodes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AssemblyNodeRead)
def create_node(payload: AssemblyNodeCreate, db: Session = Depends(get_db)):
    node = AssemblyNode(**payload.dict())
    db.add(node)
    db.commit()
    db.refresh(node)
    return node

@router.get("/", response_model=List[AssemblyNodeRead])
def list_nodes(db: Session = Depends(get_db)):
    return db.query(AssemblyNode).all()

@router.get("/{node_id}", response_model=AssemblyNodeRead)
def get_node(node_id: int, db: Session = Depends(get_db)):
    node = db.get(AssemblyNode, node_id)
    if not node:
        raise HTTPException(404, "AssemblyNode not found")
    return node

@router.put("/{node_id}", response_model=AssemblyNodeRead)
def update_node(node_id: int, payload: AssemblyNodeCreate, db: Session = Depends(get_db)):
    node = db.get(AssemblyNode, node_id)
    if not node:
        raise HTTPException(404, "AssemblyNode not found")
    for field, val in payload.dict().items():
        setattr(node, field, val)
    db.commit()
    db.refresh(node)
    return node

@router.delete("/{node_id}", status_code=204)
def delete_node(node_id: int, db: Session = Depends(get_db)):
    node = db.get(AssemblyNode, node_id)
    if not node:
        raise HTTPException(404, "AssemblyNode not found")
    db.delete(node)
    db.commit()
