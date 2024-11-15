from fastapi import FastAPI, Response, status, HTTPException, Depends
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import models
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import time
import schemas
from typing import List
from passlib.context import CryptContext
from routers import post, user, auth

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
models.Base.metadata.create_all(bind=engine)

app = FastAPI()



try:
    conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='0528', cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    print('Database connected')
except Exception as e:
    print('Connection failed')
    print('Error:', e)
    time.sleep(2)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Hello World"}



