from sqlalchemy import Column, Integer, Numeric, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.db.base import Base


class Order(Base):
    __tablename__ = "orders"
    id          = Column(Integer, primary_key=True, index=True)
    created_at  = Column(DateTime, default=datetime.utcnow)
    status      = Column(String, default="new", nullable=False)
    total_price = Column(Numeric(12,2), nullable=False, default=0)

    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")
