# schemas/part.py
from pydantic import BaseModel
from typing import Optional
from schemas.manufacturer import ManufacturerRead
from schemas.assembly_node import AssemblyNodeRead

class PartBase(BaseModel):
    name: str
    part_number: str
    description: Optional[str] = None
    price: float
    stock_quantity: int
    manufacturer_id: int
    assembly_node_id: int

class PartCreate(PartBase):
    pass

class PartRead(PartBase):
    id: int
    manufacturer: Optional[ManufacturerRead]
    assembly_node: Optional[AssemblyNodeRead]

    class Config:
        orm_mode = True
