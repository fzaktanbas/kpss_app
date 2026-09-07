from app.database import SessionLocal
from app.models.exam_type import ExamType
from app.models.test_group import TestGroup
from app.models.subject import Subject

from app.models.exam_type_subject import ExamTypeSubject
from app.models.topic import Topic


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


def seed_test_groups():
    db = SessionLocal()

    try:
        test_groups = [
            TestGroup(id=1, name="Genel Yetenek"),
            TestGroup(id=2, name="Genel Kültür"),
        ]

        for test_group in test_groups:
            existing = db.query(TestGroup).filter(
                TestGroup.id == test_group.id
            ).first()

            if not existing:
                db.add(test_group)

        db.commit()
        print("Test grupları başarıyla eklendi.")

    finally:
        db.close()


def seed_subjects():
    db = SessionLocal()

    try:
        subjects = [
            Subject(id=1, name="Türkçe"),
            Subject(id=2, name="Matematik"),
            Subject(id=3, name="Tarih"),
            Subject(id=4, name="Coğrafya"),
            Subject(id=5, name="Vatandaşlık"),
            Subject(id=6, name="Güncel Bilgiler"),
        ]

        for subject in subjects:
            existing = db.query(Subject).filter(
                Subject.id == subject.id
            ).first()

            if not existing:
                db.add(subject)

        db.commit()
        print("Dersler başarıyla eklendi.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_exam_types()
    seed_test_groups()
    seed_subjects()