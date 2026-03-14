"""
Задание №5 (средней сложности)
Абстрактный класс Animal и класс Dog, наследующий Animal.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Абстрактное животное."""
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def speak(self) -> str:
        """Издать звук."""
        pass


class Dog(Animal):
    """Собака."""
    def speak(self) -> str:
        return f"{self.name} says Woof!"


if __name__ == "__main__":
    dog = Dog("Шарик")
    print(dog.speak())