from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

class AssemblyNode(Base):
    __tablename__ = "assembly_nodes"
    id = Column(Integer, primary_key=True, index=True)
    unit_type_id = Column(Integer, ForeignKey("unit_types.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)

    unit_type = relationship("UnitType", backref="assembly_nodes")
