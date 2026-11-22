"""Єдиний журнал подій для однопотокового застосунку кіоска."""

from __future__ import annotations

from typing import ClassVar, Protocol, final


# Клієнтський контракт для запису подій.
class EventSink(Protocol):
    """Приймає повідомлення про події кіоска."""

    def record(self, message: str) -> None:
        """Додає подію до журналу."""


# Singleton
@final
class KioskEventLog:
    """Зберігає спільний журнал у межах одного процесу."""

    _instance: ClassVar[KioskEventLog | None] = None
    _events: list[str]

    def __new__(cls) -> KioskEventLog:
        """Створює журнал під час першого звернення."""
        if cls._instance is None:
            instance = super().__new__(cls)
            instance._events = []
            cls._instance = instance
        return cls._instance

    def record(self, message: str) -> None:
        """Записує подію в спільний журнал."""
        self._events.append(message)

    def events(self) -> tuple[str, ...]:
        """Повертає накопичені записи."""
        return tuple(self._events)


# Client
def register_payment(log: EventSink) -> None:
    """Фіксує отримання оплати за квиток."""
    log.record("Оплату за квиток прийнято.")


# Client
def register_ticket(log: EventSink) -> None:
    """Фіксує завершення друку квитка."""
    log.record("Квиток надруковано.")


def main() -> None:
    """Показує, що обидва компоненти використовують один журнал."""
    payment_log = KioskEventLog()
    printer_log = KioskEventLog()
    register_payment(payment_log)
    register_ticket(printer_log)

    print(f"Спільний журнал: {payment_log is printer_log}")
    print("\n".join(payment_log.events()))


if __name__ == "__main__":
    main()
