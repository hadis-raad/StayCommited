import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers import users, goals

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Set up CORS
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

app.include_router(users.router, prefix="/api", tags=["users"])
app.include_router(goals.router, prefix="/api", tags=["goals"])

@app.get("/")
def read_root():
    return {"message": "Welcome to stayComitted!"}
