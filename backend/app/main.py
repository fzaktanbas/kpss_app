from fastapi import FastAPI
from sqlalchemy import text

from app.database import Base, engine
from app.models.exam_type import ExamType
from app.models.subject import Subject
from app.models.test_group import TestGroup
from app.models.exam_type_subject import ExamTypeSubject
from app.models.topic import Topic

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():
    return {"message": "KPSS App Backend çalışıyor!"}


@app.get("/test-db")
def test_db():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"database": result.scalar()}