from sqlalchemy import Column, Integer, Text, DateTime
from datetime import datetime
from .db import Base

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    prompt = Column(Text)
    response = Column(Text)
