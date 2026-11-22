"""Створення узгоджених компонентів звіту в HTML і Markdown."""

from html import escape
from typing import Protocol


# AbstractProduct
class Heading(Protocol):
    """Заголовок звіту в певному форматі."""

    def render(self, title: str) -> str:
        """Форматує заголовок."""


# AbstractProduct
class BulletList(Protocol):
    """Маркований список звіту в певному форматі."""

    def render(self, items: tuple[str, ...]) -> str:
        """Форматує пункти списку."""


# ConcreteProduct — родина HTML
class HtmlHeading:
    """Створює заголовок HTML."""

    def render(self, title: str) -> str:
        """Екранує текст і додає тег заголовка."""
        return f"<h1>{escape(title)}</h1>"


# ConcreteProduct — родина HTML
class HtmlBulletList:
    """Створює маркований список HTML."""

    def render(self, items: tuple[str, ...]) -> str:
        """Екранує текст пунктів і оформлює їх тегами."""
        rows = "\n".join(f"  <li>{escape(item)}</li>" for item in items)
        return f"<ul>\n{rows}\n</ul>"


# ConcreteProduct — родина Markdown
class MarkdownHeading:
    """Створює заголовок Markdown."""

    def render(self, title: str) -> str:
        """Додає позначку заголовка до підготовленого тексту."""
        return f"# {title}"


# ConcreteProduct — родина Markdown
class MarkdownBulletList:
    """Створює маркований список Markdown."""

    def render(self, items: tuple[str, ...]) -> str:
        """Додає маркери до підготовлених пунктів."""
        return "\n".join(f"- {item}" for item in items)


# AbstractFactory
class ReportFactory(Protocol):
    """Створює компоненти одного формату звіту."""

    def create_heading(self) -> Heading:
        """Створює заголовок."""

    def create_bullet_list(self) -> BulletList:
        """Створює маркований список."""


# ConcreteFactory
class HtmlReportFactory:
    """Видає компоненти для звіту HTML."""

    def create_heading(self) -> Heading:
        """Створює заголовок HTML."""
        return HtmlHeading()

    def create_bullet_list(self) -> BulletList:
        """Створює список HTML."""
        return HtmlBulletList()


# ConcreteFactory
class MarkdownReportFactory:
    """Видає компоненти для звіту Markdown."""

    def create_heading(self) -> Heading:
        """Створює заголовок Markdown."""
        return MarkdownHeading()

    def create_bullet_list(self) -> BulletList:
        """Створює список Markdown."""
        return MarkdownBulletList()


# Client
def render_report(
    factory: ReportFactory, title: str, items: tuple[str, ...]
) -> str:
    """Збирає звіт із компонентів, отриманих від однієї фабрики."""
    heading = factory.create_heading().render(title)
    bullet_list = factory.create_bullet_list().render(items)
    return f"{heading}\n\n{bullet_list}"


def main() -> None:
    """Виводить один звіт у двох форматах."""
    title = "Звіт бібліотеки"
    items = ("Видано 18 книжок", "Повернено 11 книжок")
    print(render_report(HtmlReportFactory(), title, items))
    print()
    print(render_report(MarkdownReportFactory(), title, items))


if __name__ == "__main__":
    main()
