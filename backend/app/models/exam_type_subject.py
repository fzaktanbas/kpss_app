from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class ExamTypeSubject(Base):
    __tablename__ = "exam_type_subjects"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    exam_type_id = Column(
        Integer,
        ForeignKey("exam_types.id"),
        nullable=False
    )

    subject_id = Column(
        Integer,
        ForeignKey("subjects.id"),
        nullable=False
    )

    test_group_id = Column(
        Integer,
        ForeignKey("test_groups.id"),
        nullable=False
    )

    exam_type = relationship(
        "ExamType",
        back_populates="exam_type_subjects"
    )

    subject = relationship(
        "Subject",
        back_populates="exam_type_subjects"
    )

    test_group = relationship(
        "TestGroup",
        back_populates="exam_type_subjects"
    )