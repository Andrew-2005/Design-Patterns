"""Оформлення доставки різними видами транспорту."""

from abc import ABC, abstractmethod
from typing import Protocol


# Product
class Transport(Protocol):
    """Спільний контракт для засобів доставки."""

    def deliver(self, cargo: str, destination: str) -> str:
        """Повертає повідомлення про доставку вантажу."""


# ConcreteProduct
class Truck:
    """Вантажівка для наземної доставки."""

    def deliver(self, cargo: str, destination: str) -> str:
        """Описує доставку автомобілем."""
        return f"Вантажівка везе вантаж «{cargo}» до міста {destination}."


# ConcreteProduct
class Ship:
    """Судно для морської доставки."""

    def deliver(self, cargo: str, destination: str) -> str:
        """Описує доставку морем."""
        return f"Судно везе вантаж «{cargo}» до порту {destination}."


# Creator
class Logistics(ABC):
    """Оформлює доставку через транспорт, створений підкласом."""

    @abstractmethod
    def create_transport(self) -> Transport:
        """Фабричний метод для створення транспорту."""

    def dispatch(self, cargo: str, destination: str) -> str:
        """Оформлює відправлення і передає вантаж транспорту."""
        transport = self.create_transport()
        delivery = transport.deliver(cargo, destination)
        return f"Відправлення оформлено. {delivery}"


# ConcreteCreator
class RoadLogistics(Logistics):
    """Організовує наземні перевезення."""

    def create_transport(self) -> Transport:
        """Створює вантажівку для відправлення."""
        return Truck()


# ConcreteCreator
class SeaLogistics(Logistics):
    """Організовує морські перевезення."""

    def create_transport(self) -> Transport:
        """Створює судно для відправлення."""
        return Ship()


def main() -> None:
    """Оформлює відправлення для двох маршрутів."""
    print(RoadLogistics().dispatch("книги", "Львів"))
    print(SeaLogistics().dispatch("обладнання", "Одеса"))


if __name__ == "__main__":
    main()
