from sqlalchemy import Column, Integer, String, ForeignKey

from app.database import Base


class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    exam_type_id = Column(
        Integer,
        ForeignKey("exam_types.id"),
        nullable=False
    )