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

@router.post("/goals/", response_model=schemas.Goal)
def create_goal(goal: schemas.GoalCreate, db: Session = Depends(get_db)):
    return crud.create_goal(db=db, goal=goal)

@router.get("/goals/", response_model=List[schemas.Goal])
def read_goals(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    goals = crud.get_goals(db, skip=skip, limit=limit)
    return goals
