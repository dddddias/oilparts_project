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