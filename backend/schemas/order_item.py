from pydantic import BaseModel

class OrderItemBase(BaseModel):
    part_id: int
    quantity: int

class OrderItemCreate(OrderItemBase):
    pass

class OrderItemRead(OrderItemBase):
    id: int
    unit_price: float

    class Config:
        orm_mode = True
