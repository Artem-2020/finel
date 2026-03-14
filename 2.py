"""
Лабораторная работа №2
Вариант 10: задания №2,5,10 (средние) и №1,4 (повышенные)
Автор: [Ваше ФИО]
"""

import matplotlib.pyplot as plt
import numpy as np


# ---------- Задание 10 (средний): Словарь квадратов чисел ----------
def dict_of_squares(n: int) -> dict:
    """
    Возвращает словарь, где ключ – число от 1 до n,
    а значение – квадрат этого числа.
    """
    return {i: i ** 2 for i in range(1, n + 1)}


# ---------- Задание 2 (средний): Сумма нечётных чисел до N ----------
def sum_of_odds(n: int) -> int:
    """
    Вычисляет сумму всех нечётных чисел от 1 до n включительно.
    """
    total = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            total += i
    return total


# ---------- Задание 5 (средний): Список простых чисел до 100 ----------
def prime_list(limit: int = 100) -> list:
    """
    Возвращает список простых чисел от 2 до limit,
    используя алгоритм "Решето Эратосфена".
    """

    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False

    return [num for num, is_prime in enumerate(sieve) if is_prime]


# ---------- Задание 1 (повышенный): Сортировка пузырьком ----------
def bubble_sort(arr: list) -> list:
    """
    Сортирует список методом пузырька (по возрастанию).
    Возвращает новый отсортированный список (исходный не меняется).
    """

    arr_copy = arr.copy()
    n = len(arr_copy)

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
        if not swapped:
            break
    return arr_copy


# ---------- Задание 4 (повышенный): График y = x² ----------
def plot_parabola():
    """
    Строит график функции y = x² на интервале [-10, 10]
    с использованием matplotlib.
    """
    # Генерация 200 точек на отрезке [-10, 10]
    x = np.linspace(-10, 10, 200)
    y = x ** 2

    # Построение графика
    plt.plot(x, y, label='y = x²', color='blue', linewidth=2)
    plt.title('График функции y = x²')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    # Отметить нулевые оси
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    # Показать окно с графиком
    plt.show()


# ---------- Основная часть программы ----------
if __name__ == "__main__":
    # Задание 10: словарь квадратов
    n_sq = 10
    squares = dict_of_squares(n_sq)
    print(f"1. Словарь квадратов чисел от 1 до {n_sq}:")
    print(squares)
    print()

    # Задание 2: сумма нечётных
    n_odd = 15
    odd_sum = sum_of_odds(n_odd)
    print(f"2. Сумма нечётных чисел от 1 до {n_odd} = {odd_sum}")
    print()

    # Задание 5: простые числа
    primes = prime_list(100)
    print(f"3. Простые числа до 100 (всего {len(primes)}):")
    print(primes)
    print()

    # Задание 1: сортировка пузырьком
    test_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = bubble_sort(test_list)
    print("4. Сортировка пузырьком:")
    print(f"   Исходный список: {test_list}")
    print(f"   Отсортированный: {sorted_list}")
    print()

    # Задание 4: график
    print("5. Закрытие окна с графиком продолжит выполнение программы.")
    plot_parabola()
    print("Программа завершена.")
