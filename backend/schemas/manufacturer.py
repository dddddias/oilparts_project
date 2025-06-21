# schemas/manufacturer.py
from pydantic import BaseModel
from typing import Optional

class ManufacturerBase(BaseModel):
    name: str
    country: Optional[str] = None

class ManufacturerCreate(ManufacturerBase):
    pass

class ManufacturerRead(ManufacturerBase):
    id: int

    class Config:
        orm_mode = True
