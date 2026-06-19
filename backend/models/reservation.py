from datetime import datetime

from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String, UniqueConstraint

from backend.database import Base


class Reservation(Base):
    __tablename__ = "reservations"
    __table_args__ = (
        UniqueConstraint("user_id", "book_id", name="unique_user_book_reservation"),
    )

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    reservation_date = Column(Date, nullable=False)
    status = Column(String(20), default="reserved")
    created_at = Column(DateTime, default=datetime.utcnow)

