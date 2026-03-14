from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создаём движок и базовый класс
engine = create_engine('sqlite:///lab7_orm.db', echo=True)
Base = declarative_base()


# Определяем модель Student
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    grade = Column(Float)

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', age={self.age}, grade={self.grade})>"


# Создаём таблицу
Base.metadata.create_all(engine)

# Создаём сессию
Session = sessionmaker(bind=engine)
session = Session()

# --- CREATE ---
print("Добавляем студентов...")
student1 = Student(name='Ольга Новикова', age=22, grade=4.8)
student2 = Student(name='Дмитрий Волков', age=20, grade=3.9)
session.add_all([student1, student2])
session.commit()
print("Студенты добавлены.")

# --- READ ---
print("\nВсе студенты:")
students = session.query(Student).all()
for s in students:
    print(s)

# --- UPDATE ---
print("\nОбновляем оценку студента с id=1...")
student_to_update = session.query(Student).filter_by(id=1).first()
if student_to_update:
    student_to_update.grade = 5.0
    session.commit()
    print("Обновлено:", student_to_update)

# --- DELETE ---
print("\nУдаляем студента с id=2...")
student_to_delete = session.query(Student).filter_by(id=2).first()
if student_to_delete:
    session.delete(student_to_delete)
    session.commit()
    print("Студент удалён.")

# Проверяем итоговое состояние
print("\nИтоговый список студентов:")
students = session.query(Student).all()
for s in students:
    print(s)

session.close()