# models/part.py
from sqlalchemy import Column, Integer, String, Text, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from backend.db.base import Base

class Part(Base):
    __tablename__ = "parts"
    id               = Column(Integer, primary_key=True, index=True)
    name             = Column(String, nullable=False)
    part_number      = Column(String, nullable=False, unique=True, index=True)
    description      = Column(Text, nullable=True)
    price            = Column(Numeric(12, 2), nullable=False)
    stock_quantity   = Column(Integer, nullable=False, default=0)
    manufacturer_id  = Column(Integer, ForeignKey("manufacturers.id"), nullable=False)
    assembly_node_id = Column(Integer, ForeignKey("assembly_nodes.id"), nullable=False)

    manufacturer     = relationship("Manufacturer", backref="parts")
    assembly_node    = relationship("AssemblyNode", backref="parts")
