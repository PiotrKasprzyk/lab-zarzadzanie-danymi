from schemas import UserBase, UserDisplay
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user
from typing import List

router = APIRouter(prefix='/user', tags=['user'])

# Create user
@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

# Read ALL users
@router.get('/', response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)

# Read ONE / SELECTED user
@router.get('/{id}', response_model=UserDisplay)
def get_selected_user(id: int, db: Session=Depends(get_db)):
    return db_user.get_user(db, id)

# Update user - use .PUT and/or .POST
#@router.post('/update/{id}')
@router.put('/update/{id}')
def update_user(id: int, request: UserBase, db: Session=Depends(get_db)):
    return db_user.update_user(db, id, request)

# Delete user - use .GET and/or .DELETE
#@router.get('/delete/{id}')
@router.delete('/delete/{id}')
def delete_user(id: int, db: Session=Depends(get_db)):
    return db_user.delete_user(db, id)