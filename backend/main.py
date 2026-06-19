from fastapi import FastAPI

from backend import models  
from backend.database import Base, engine
from backend.user_routes import router as user_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Library Management System API",
    version="1.0.0",
)

app.include_router(user_router)


@app.get("/")
def health_check():
    return {"message": "Library Management System API is running successfully"}

