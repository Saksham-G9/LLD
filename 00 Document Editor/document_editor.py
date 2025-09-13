from abc import ABC, abstractmethod


class Element(ABC):
    @abstractmethod
    def render(self): ...


class TextElement(Element):
    def __init__(self, text):
        self.text = text
        super().__init__()

    def render(self):
        print(f"Rendering text {self.text}")


class ImageElement(Element):
    def __init__(self, path):
        self.path = path
        super().__init__()

    def render(self):
        print(f"Rendering image at path {self.path}")


class Persistence(ABC):
    @abstractmethod
    def save(self): ...


class SQLPersistence(Persistence):
    def save(self, elements: Element):
        # can add saving logic
        print("Saving Data to SQL", elements)


class NoSQLPersistence(Persistence):
    def save(self, elements: Element):
        # can add saving logic
        print("Saving Data to NoSQL", elements)


class DocumentEditor:
    def __init__(self, persistence: Persistence):
        self._elements: list[Element] = []
        self.persistance = persistence

    def add_element(self, element: Element) -> None:
        self._elements.append(element)

    def remove_element(self, index: int) -> None:
        if 0 <= index < len(self._elements):
            self._elements.pop(index)

    def render(self) -> None:
        print("=== Document Rendering ===")
        for element in self._elements:
            element.render()
        print("=== End Document ===")

    def save(self):
        self.persistance.save(self._elements)


doc = DocumentEditor(SQLPersistence())

text = TextElement("Saksham Gupta")
image = ImageElement("./images/saksham.png")

doc.add_element(text)
doc.add_element(image)

doc.render()
doc.save()
