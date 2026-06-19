from sqlalchemy import Column, ForeignKey, Integer, String

from backend.database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    author = Column(String(150), nullable=False)
    isbn = Column(String(20), unique=True, nullable=False)
    publication_year = Column(Integer, nullable=False)
    genre = Column(String(100), nullable=False)
    main_category = Column(String(100), nullable=False)
    sub_category = Column(String(100), nullable=False)
    shelf = Column(Integer, nullable=False)
    row = Column(Integer, nullable=False)
    section = Column(String(50), nullable=False)
    total_copies = Column(Integer, nullable=False)
    available_copies = Column(Integer, nullable=False)
    damaged_copies = Column(Integer, default=0)
    lost_copies = Column(Integer, default=0)
    age_restriction = Column(Integer, default=0)
    membership_restriction = Column(String(20), nullable=True)
    borrowing_limit = Column(Integer, nullable=False)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"), nullable=False)

