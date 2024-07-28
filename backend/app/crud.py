from sqlalchemy.orm import Session
from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        username=user.username,
        email=user.email,
        password=user.password  # Ensure to hash passwords in real applications
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user: schemas.UserUpdate, user_id: int):
    db_user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if db_user:
        db_user.username = user.username
        db_user.email = user.email
        if user.password:
            db_user.password = user.password  # Ensure to hash passwords in real applications
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()

def create_goal(db: Session, goal: schemas.GoalCreate):
    db_goal = models.Goal(
        user_id=goal.user_id,
        title=goal.title,
        description=goal.description,
        start_date=goal.start_date,
        end_date=goal.end_date,
        status=goal.status
    )
    db.add(db_goal)
    db.commit()
    db.refresh(db_goal)
    return db_goal

def get_goals(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Goal).offset(skip).limit(limit).all()

def create_habit(db: Session, habit: schemas.HabitCreate):
    db_habit = models.Habit(
        user_id=habit.user_id,
        goal_id=habit.goal_id,
        name=habit.name,
        frequency=habit.frequency
    )
    db.add(db_habit)
    db.commit()
    db.refresh(db_habit)
    return db_habit

def get_habits(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Habit).offset(skip).limit(limit).all()
