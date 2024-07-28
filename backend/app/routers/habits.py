from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, models, schemas, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/habits/", response_model=schemas.Habit)
def create_habit(habit: schemas.HabitCreate, db: Session = Depends(get_db)):
    return crud.create_habit(db=db, habit=habit)

@router.get("/habits/", response_model=List[schemas.Habit])
def read_habits(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    habits = crud.get_habits(db, skip=skip, limit=limit)
    return habits
