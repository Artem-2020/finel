from functools import reduce
from typing import List


def sum_with_reduce(numbers: List[int]) -> int:
    """Возвращает сумму чисел списка с помощью reduce."""
    return reduce(lambda acc, x: acc + x, numbers, 0)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    total = sum_with_reduce(nums)
    print("Сумма чисел:", total)