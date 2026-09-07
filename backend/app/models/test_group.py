from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class TestGroup(Base):
    __tablename__ = "test_groups"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(
        String,
        unique=True,
        nullable=False
    )

    exam_type_subjects = relationship(
        "ExamTypeSubject",
        back_populates="test_group"
    )