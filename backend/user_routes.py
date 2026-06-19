from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models.user import User


router = APIRouter(prefix="/users", tags=["Users"])


class UserCreate(BaseModel):
    name: str
    email: str
    phone: str
    address: str
    age: int
    role: str = "member"
    membership_type: str = "basic"


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    age: Optional[int] = None
    role: Optional[str] = None
    membership_type: Optional[str] = None
    membership_status: Optional[str] = None
    status: Optional[str] = None


def user_to_dictionary(user):
    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "phone": user.phone,
        "address": user.address,
        "age": user.age,
        "role": user.role,
        "membership_type": user.membership_type,
        "membership_status": user.membership_status,
        "status": user.status,
        "created_at": user.created_at,
    }


@router.post("/")
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    existing_email = db.query(User).filter(User.email == user_data.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already exists")

    existing_phone = db.query(User).filter(User.phone == user_data.phone).first()
    if existing_phone:
        raise HTTPException(status_code=400, detail="Phone number already exists")

    new_user = User(
        name=user_data.name,
        email=user_data.email,
        phone=user_data.phone,
        address=user_data.address,
        age=user_data.age,
        role=user_data.role,
        membership_type=user_data.membership_type,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return user_to_dictionary(new_user)


@router.get("/")
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return [user_to_dictionary(user) for user in users]


@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user_to_dictionary(user)


@router.put("/{user_id}")
def update_user(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db),
):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user_data.name is not None:
        user.name = user_data.name
    if user_data.email is not None:
        user.email = user_data.email
    if user_data.phone is not None:
        user.phone = user_data.phone
    if user_data.address is not None:
        user.address = user_data.address
    if user_data.age is not None:
        user.age = user_data.age
    if user_data.role is not None:
        user.role = user_data.role
    if user_data.membership_type is not None:
        user.membership_type = user_data.membership_type
    if user_data.membership_status is not None:
        user.membership_status = user_data.membership_status
    if user_data.status is not None:
        user.status = user_data.status

    db.commit()
    db.refresh(user)

    return user_to_dictionary(user)


@router.delete("/{user_id}")
def deactivate_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.status = "inactive"
    db.commit()

    return {"message": "User deactivated successfully"}
