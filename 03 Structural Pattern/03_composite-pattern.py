from abc import ABC, abstractmethod


class Element(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def open(self, depth: int = 0) -> str: ...


class File(Element):
    def open(self, depth: int = 0) -> str:
        prefix = "  " * depth
        return f"{prefix}{self.name}"


class Folder(Element):
    def __init__(self, name: str):
        super().__init__(name)
        self.elements: list[Element] = []

    def open(self, depth: int = 0) -> str:
        prefix = "  " * depth
        result = [f"{prefix}{self.name}/"]
        if not self.elements:
            result.append(f"{prefix}  (empty)")
        for el in self.elements:
            result.append(el.open(depth + 1))
        return "\n".join(result)

    def add(self, element: Element):
        self.elements.append(element)


# --- Client code ---
f1, f2, f3 = File("file1.txt"), File("file2.txt"), File("file3.txt")
folder1 = Folder("Folder1")
folder2 = Folder("Folder2")

folder1.add(f1)
folder1.add(folder2)
folder2.add(f2)
folder2.add(f3)

print(folder1.open())
