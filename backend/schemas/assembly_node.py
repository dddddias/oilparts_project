from pydantic import BaseModel
from typing import Optional
from schemas.unit_type import UnitTypeRead

class AssemblyNodeBase(BaseModel):
    name: str
    description: Optional[str] = None
    unit_type_id: int

class AssemblyNodeCreate(AssemblyNodeBase):
    pass

class AssemblyNodeRead(AssemblyNodeBase):
    id: int
    unit_type: Optional[UnitTypeRead]  # вложенный объект

    class Config:
        orm_mode = True
