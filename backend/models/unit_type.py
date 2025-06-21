from sqlalchemy import Column, Integer, String, Text
from db.base import Base

class UnitType(Base):
    __tablename__ = "unit_types"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
