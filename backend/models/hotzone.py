from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

class Hotzone(Base):
    __tablename__ = "hotzones"
    id        = Column(Integer, primary_key=True, index=True)
    drawing   = Column(Integer, nullable=False)             # ID самой схемы, если их несколько
    part_id   = Column(Integer, ForeignKey("parts.id"), nullable=False)
    x         = Column(Integer, nullable=False)
    y         = Column(Integer, nullable=False)
    width     = Column(Integer, nullable=False)
    height    = Column(Integer, nullable=False)
    number    = Column(Integer, nullable=False)             # цифра, которая будет на картинке

    part      = relationship("Part", backref="hotzones")