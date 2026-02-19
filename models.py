from sqlalchemy import Column, Integer, String, Boolean, Float
from database import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True)
    description = Column(String(255))
    price = Column(Float)
    is_active = Column(Boolean, default=True)

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(255))
    is_active = Column(Boolean, default=True)
