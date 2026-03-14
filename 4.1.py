from typing import List


def squares_map() -> List[int]:
    """Возвращает список квадратов чисел от 1 до 10 с использованием map."""
    numbers = range(1, 11)
    squares = list(map(lambda x: x**2, numbers))
    return squares


if __name__ == "__main__":
    result = squares_map()
    print("Квадраты чисел 1-10:", result)