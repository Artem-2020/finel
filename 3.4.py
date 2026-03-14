"""
Задание №1 (повышенной сложности)
Реализация паттерна Singleton на примере класса Config.
"""

class Config:
    """Единственный экземпляр конфигурации приложения."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self.app_name = "Lab3 App"
        self.version = "1.0.0"
        self.debug = True

    def get_config(self) -> dict:
        return {
            "app_name": self.app_name,
            "version": self.version,
            "debug": self.debug
        }


# Пример автономного использования
if __name__ == "__main__":
    c1 = Config()
    c2 = Config()
    print(c1 is c2)  # True – один и тот же объект
    print(c1.get_config())