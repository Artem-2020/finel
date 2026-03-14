from typing import Callable, Dict, Any


def memoize(func: Callable) -> Callable:
    """Декоратор, кэширующий результаты вызова функции."""
    cache: Dict[Any, Any] = {}

    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper


@memoize
def fibonacci(n: int) -> int:
    """Рекурсивное вычисление числа Фибоначчи."""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    n = 35
    result = fibonacci(n)
    print(f"fibonacci({n}) = {result}")

    import time
    start = time.time()
    result2 = fibonacci(n)
    elapsed = time.time() - start
    print(f"Повторный вызов занял {elapsed:.6f} сек.")