from sqlalchemy import Column, Integer, String, Boolean, Float
from database import Base

class Course(Base):
    __tablename__ = "course"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    Instructor = Column(String, nullable=False)
    Duration = Column(Integer, nullable=False)
    website = Column(String, nullable=True)

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(255))
    is_active = Column(Boolean, default=True)
