from typing import Callable, Any


def compose(*funcs: Callable) -> Callable:
    """
    Возвращает функцию, являющуюся композицией переданных функций.
    Композиция выполняется справа налево: compose(f, g)(x) = f(g(x))
    """
    def composed(x: Any) -> Any:
        result = x
        for f in reversed(funcs):
            result = f(result)
        return result
    return composed


def add_one(x):
    return x + 1


def square(x):
    return x ** 2


def double(x):
    return x * 2


if __name__ == "__main__":
    f = compose(add_one, square, double)
    x = 3
    result = f(x)
    print(f"compose(add_one, square, double)({x}) = {result}")

    g = compose(double, square, add_one)
    result2 = g(x)
    print(f"compose(double, square, add_one)({x}) = {result2}")