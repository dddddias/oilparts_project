from sqlalchemy import Column, Integer, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

class OrderItem(Base):
    __tablename__ = "order_items"
    id        = Column(Integer, primary_key=True, index=True)
    order_id  = Column(Integer, ForeignKey("orders.id"), nullable=False)
    part_id   = Column(Integer, ForeignKey("parts.id"), nullable=False)
    quantity  = Column(Integer, nullable=False)
    unit_price = Column(Numeric(12,2), nullable=False)

    order = relationship("Order", back_populates="items")
    part  = relationship("Part")
