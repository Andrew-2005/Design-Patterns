"""Покрокове складання плану навчальної екскурсії."""

from dataclasses import dataclass
from typing import Protocol


# Product
@dataclass(frozen=True)
class Excursion:
    """Готовий маршрут із переліком зупинок і транспортом."""

    title: str
    stops: tuple[str, ...]
    transport: str


# Builder
class ExcursionBuilder(Protocol):
    """Описує кроки складання плану екскурсії."""

    def add_stop(self, stop: str) -> None:
        """Додає зупинку до маршруту."""

    def set_transport(self, transport: str) -> None:
        """Обирає транспорт для групи."""

    def build(self) -> Excursion:
        """Повертає готовий план."""


# ConcreteBuilder
class RouteBuilder:
    """Накопичує зупинки й перевіряє готовність маршруту."""

    def __init__(self, title: str) -> None:
        """Починає порожній маршрут із пішим пересуванням."""
        self._title = title
        self._stops: list[str] = []
        self._transport = "пішки"

    def add_stop(self, stop: str) -> None:
        """Додає зупинку в кінець маршруту."""
        self._stops.append(stop)

    def set_transport(self, transport: str) -> None:
        """Задає спосіб пересування."""
        self._transport = transport

    def build(self) -> Excursion:
        """Перевіряє наявність зупинок і фіксує готовий план."""
        if not self._stops:
            raise ValueError("Маршрут має містити щонайменше одну зупинку.")
        return Excursion(self._title, tuple(self._stops), self._transport)


# Director
def plan_city_excursion(builder: ExcursionBuilder) -> Excursion:
    """Застосовує готову послідовність кроків для міської екскурсії."""
    builder.set_transport("автобус")
    builder.add_stop("Історичний музей")
    builder.add_stop("Міська ратуша")
    return builder.build()


def main() -> None:
    """Складає маршрут і виводить його в консоль."""
    builder = RouteBuilder("Історія міста")
    excursion = plan_city_excursion(builder)
    print(f"Екскурсія «{excursion.title}», транспорт: {excursion.transport}")
    print(" → ".join(excursion.stops))


if __name__ == "__main__":
    main()
