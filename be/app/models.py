# be/models.py
from sqlalchemy import Column, Integer, String, Text, ForeignKey, TIMESTAMP, func
from sqlalchemy.orm import relationship
from .db import Base

class Sender(Base):
    __tablename__ = "sender"

    id = Column(Integer, primary_key=True, index=True)
    line_user_id = Column(String(50), unique=True, nullable=True)
    display_name = Column(String(255), nullable=True)

    chats = relationship("Chat", back_populates="sender", cascade="all, delete")

class Chat(Base):
    __tablename__ = "chat"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    sender_id = Column(Integer, ForeignKey("sender.id", ondelete="CASCADE"), nullable=False)

    sender = relationship("Sender", back_populates="chats")
