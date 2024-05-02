from fastapi import FastAPI
import models
from database import engine,SessionLocal
from pydantic import BaseModel,Field
from sqlalchemy.orm import session
from routers import students,faculty,auth
import uuid
app=FastAPI(
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redocs",
    title="STUDENT DATABASE MANAGEMENT APP",
    description="A simple student server based student database management  app",
    version="2.0",
    openapi_url="/api/v1/openapi.json"
)

app.include_router(students.router)
app.include_router(faculty.router)
app.include_router(auth.router)

    
