from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = "sqlite:///./library.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


def get_db():
    """Provide one database session for each API request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

