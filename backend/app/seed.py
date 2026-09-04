from app.database import SessionLocal
from app.models.exam_type import ExamType


def seed_exam_types():
    db = SessionLocal()

    try:
        exam_types = [
            ExamType(id=1, name="KPSS Ortaöğretim"),
            ExamType(id=2, name="KPSS Lisans"),
            ExamType(id=3, name="KPSS Önlisans"),
        ]

        for exam_type in exam_types:
            existing = db.query(ExamType).filter(
                ExamType.id == exam_type.id
            ).first()

            if not existing:
                db.add(exam_type)

        db.commit()
        print("Sınav türleri başarıyla eklendi.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_exam_types()