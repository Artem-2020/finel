"""
Задание №10 (средней сложности)
Класс StudentRepository, реализующий итератор для перебора студентов.
"""

from typing import List, Optional, Iterator
"""
Задание №10 (средней сложности)
Класс StudentRepository, реализующий итератор для перебора студентов.
"""
from typing import List, Optional, Iterator


class Student:
    """Класс, представляющий студента."""
    def __init__(self, student_id: int, name: str, age: int):
        self.id = student_id
        self.name = name
        self.age = age

    def info(self) -> str:
        """Возвращает информацию о студенте."""
        return f"Student(id={self.id}, name='{self.name}', age={self.age})"


if __name__ == "__main__":
    s = Student(1, "Иван Петров", 20)


class StudentRepository:
    """Репозиторий студентов с поддержкой итерации."""
    def __init__(self):
        self._storage: dict[int, Student] = {}
        self._counter = 0

    def add(self, student: Student) -> Student:
        self._counter += 1
        student.id = self._counter
        self._storage[student.id] = student
        return student

    def get(self, student_id: int) -> Optional[Student]:
        return self._storage.get(student_id)

    def get_all(self) -> List[Student]:
        return list(self._storage.values())

    def __iter__(self) -> Iterator[Student]:
        """Возвращает итератор по студентам."""
        return iter(self._storage.values())


# Пример автономного использования
if __name__ == "__main__":
    repo = StudentRepository()
    repo.add(Student(0, "Анна", 19))
    repo.add(Student(0, "Борис", 21))

    print("Перебор студентов через итератор:")
    for student in repo:
        print(student.info())
