from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None  # Allow password to be optional for updates

class User(UserBase):
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class GoalBase(BaseModel):
    title: str
    description: Optional[str]
    start_date: Optional[date]
    end_date: Optional[date]
    status: str

class GoalCreate(GoalBase):
    user_id: int

class Goal(GoalBase):
    goal_id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class HabitBase(BaseModel):
    name: str
    frequency: str

class HabitCreate(HabitBase):
    user_id: int
    goal_id: int

class Habit(HabitBase):
    habit_id: int
    user_id: int
    goal_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
