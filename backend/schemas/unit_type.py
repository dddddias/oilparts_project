from pydantic import BaseModel
from typing import Optional

class UnitTypeBase(BaseModel):
    name: str
    description: Optional[str] = None

class UnitTypeCreate(UnitTypeBase):
    pass

class UnitTypeRead(UnitTypeBase):
    id: int

    class Config:
        orm_mode = True
