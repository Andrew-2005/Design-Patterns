"""Створення варіантів контрольної роботи зі спільного шаблону."""

from copy import deepcopy
from dataclasses import dataclass
from typing import Protocol, Self


# Prototype
class QuizPrototype(Protocol):
    """Описує можливість створити незалежний варіант роботи."""

    def clone(self, title: str) -> Self:
        """Повертає копію під новою назвою."""


# ConcretePrototype
@dataclass
class Quiz(QuizPrototype):
    """Містить назву роботи й варіанти відповідей для кожного питання."""

    title: str
    answers: dict[str, list[str]]

    def clone(self, title: str) -> Self:
        """Копіює роботу разом із вкладеними списками відповідей."""
        variant = deepcopy(self)
        variant.title = title
        return variant


# Client
def main() -> None:
    """Змінює копію роботи й показує, що шаблон зберігся."""
    question = "Яка столиця України?"
    template = Quiz("Шаблон", {question: ["Київ", "Львів", "Одеса"]})
    variant = template.clone("Варіант А")
    variant.answers[question].reverse()

    for quiz in (template, variant):
        print(f"{quiz.title}: {', '.join(quiz.answers[question])}")


if __name__ == "__main__":
    main()
