from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base


class Toy(Base):
    __tablename__ = "toys"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    in_stock = Column(Boolean, default=True)
