from typing import List


def filter_even(numbers: List[int]) -> List[int]:
    """Возвращает список чётных чисел из исходного списка."""
    return list(filter(lambda x: x % 2 == 0, numbers))


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens = filter_even(nums)
    print("Чётные числа:", evens)