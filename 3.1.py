"""
Задание №2 (средней сложности)
Класс Student с полями id, имя, возраст и методом info().
"""


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
    print(s.info())