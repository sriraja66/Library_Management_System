from sqlalchemy import Column, Date, Integer, String

from backend.database import Base


class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    contact_info = Column(String(100), nullable=False)
    joining_date = Column(Date, nullable=False)
    address = Column(String(255), nullable=False)
    status = Column(String(20), default="active")

