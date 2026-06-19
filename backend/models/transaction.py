from datetime import datetime

from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String

from backend.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    issued_by_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    issue_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)
    return_date = Column(Date, nullable=True)
    status = Column(String(20), default="issued")
    created_at = Column(DateTime, default=datetime.utcnow)

