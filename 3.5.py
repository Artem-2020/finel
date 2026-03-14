"""
Задание №4 (повышенной сложности)
Паттерн Strategy для расчёта цены со скидкой.
Дополнительно: сетевой сервис (имитация API) для получения внешней скидки.
"""

from abc import ABC, abstractmethod
import asyncio
import random
import sys


class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, base_price: float) -> float:
        pass


class NoDiscount(DiscountStrategy):
    def apply_discount(self, base_price: float) -> float:
        return base_price


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: float):
        self.percent = percent

    def apply_discount(self, base_price: float) -> float:
        return base_price * (1 - self.percent / 100)


class FixedDiscount(DiscountStrategy):
    def __init__(self, amount: float):
        self.amount = amount

    def apply_discount(self, base_price: float) -> float:
        return max(0, base_price - self.amount)


class ApiClient:
    """Клиент для получения скидки из внешнего API."""
    def __init__(self, base_url: str = "https://api.example.com"):
        self.base_url = base_url

    async def get_discount_percent(self) -> float:
        """Имитация асинхронного запроса к API."""
        await asyncio.sleep(0.1)
        return random.uniform(0, 20)


class PriceService:
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client

    async def calculate_price(self, base_price: float, strategy: DiscountStrategy = None) -> dict:
        if strategy is None:
            strategy = NoDiscount()

        price_after_strategy = strategy.apply_discount(base_price)
        api_discount_percent = await self.api_client.get_discount_percent()
        api_discount = price_after_strategy * (api_discount_percent / 100)
        final_price = price_after_strategy - api_discount

        return {
            "base_price": base_price,
            "strategy_discount": round(base_price - price_after_strategy, 2),
            "api_discount_percent": round(api_discount_percent, 2),
            "api_discount": round(api_discount, 2),
            "final_price": round(final_price, 2)
        }


async def demo():
    client = ApiClient()
    service = PriceService(client)

    result1 = await service.calculate_price(1000, PercentageDiscount(15))
    print("Результат с процентной скидкой 15%:", result1)

    result2 = await service.calculate_price(1000, FixedDiscount(200))
    print("Результат с фиксированной скидкой 200:", result2)

    result3 = await service.calculate_price(1000)
    print("Результат без скидки:", result3)

if __name__ == "__main__":
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        asyncio.run(demo())
    else:
        loop.create_task(demo())
