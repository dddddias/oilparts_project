# routers/orders.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from decimal import Decimal
from typing import List

from backend.db.session import SessionLocal
from models.order import Order
from models.order_item import OrderItem
from models.part import Part                           # ← импортируем Part
from schemas.order import OrderCreate, OrderRead
from schemas.order_item import OrderItemCreate, OrderItemRead  # ← импортируем OrderItemCreate, OrderItemRead


router = APIRouter(prefix="/orders", tags=["orders"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=OrderRead)
def create_order(payload: OrderCreate, db: Session = Depends(get_db)):
    # 1) создаём заказ без total_price
    order = Order(status=payload.status)
    db.add(order)
    db.flush()  # получаем order.id

    total = Decimal(0)
    for item in payload.items:
        part = db.get(Part, item.part_id)
        if not part:
            raise HTTPException(404, f"Part {item.part_id} not found")
        unit_price = part.price
        total += unit_price * item.quantity
        db.add(OrderItem(
            order_id=order.id,
            part_id=item.part_id,
            quantity=item.quantity,
            unit_price=unit_price
        ))

    order.total_price = total
    db.commit()
    db.refresh(order)
    return order

@router.get("/", response_model=List[OrderRead])
def list_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()

@router.get("/{order_id}", response_model=OrderRead)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.get(Order, order_id)
    if not order:
        raise HTTPException(404, "Order not found")
    return order

@router.delete("/{order_id}", status_code=204)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    order = db.get(Order, order_id)
    if not order:
        raise HTTPException(404, "Order not found")
    db.delete(order)
    db.commit()
