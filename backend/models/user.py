from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from backend.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(20), unique=True, nullable=False)
    address = Column(String(255), nullable=False)
    age = Column(Integer, nullable=False)
    role = Column(String(20), default="member")
    membership_type = Column(String(20), default="basic")
    membership_status = Column(String(20), default="active")
    status = Column(String(20), default="active")
    created_at = Column(DateTime, default=datetime.utcnow)

