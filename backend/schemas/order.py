from pydantic import BaseModel
from typing import List
from datetime import datetime
from schemas.order_item import OrderItemCreate, OrderItemRead

class OrderBase(BaseModel):
    status: str = "new"

class OrderCreate(OrderBase):
    items: List[OrderItemCreate]

class OrderRead(OrderBase):
    id: int
    created_at: datetime
    total_price: float
    items: List[OrderItemRead]

    class Config:
        orm_mode = True

