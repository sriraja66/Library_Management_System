from sqlalchemy import Column, Date, ForeignKey, Integer, Numeric, String

from backend.database import Base


class Fine(Base):
    __tablename__ = "fines"

    id = Column(Integer, primary_key=True)
    transaction_id = Column(
        Integer,
        ForeignKey("transactions.id"),
        unique=True,
        nullable=False,
    )
    amount = Column(Numeric(10, 2), nullable=False)
    calculated_date = Column(Date, nullable=False)
    status = Column(String(20), default="unpaid")

