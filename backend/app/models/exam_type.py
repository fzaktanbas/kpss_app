from sqlalchemy import Column, Integer, String

from app.database import Base


class ExamType(Base):
    __tablename__ = "exam_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)