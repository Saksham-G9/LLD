class Editor:
    def __init__(self):
        self.text = ""
        self.cursor = 0
        self.font_size = 12
        self.bold = False

    def type(self, words: str) -> None:
        self.text += words
        self.cursor = len(self.text)

    def toggle_bold(self):
        self.bold = not self.bold

    def set_font(self, size: int):
        self.font_size = size

    def save(self):
        return Memento(self.text, self.cursor, self.font_size, self.bold)

    def restore(self, memento: "Memento"):
        state = memento.get_state()
        self.text = state["text"]
        self.cursor = state["cursor"]
        self.font_size = state["font_size"]
        self.bold = state["bold"]


class Memento:
    def __init__(self, text, cursor, font_size, bold):
        self._state = {
            "text": text,
            "cursor": cursor,
            "font_size": font_size,
            "bold": bold,
        }

    def get_state(self):
        return self._state


class History:
    def __init__(self):
        self.stack = []

    def push(self, memento: Memento):
        self.stack.append(memento)

    def pop(self):
        return self.stack.pop() if self.stack else None


editor = Editor()
history = History()

editor.type("Hello")
editor.set_font(14)
editor.toggle_bold()

history.push(editor.save())


editor.type("World!")
editor.set_font(18)
history.push(editor.save())

editor.restore(history.pop())
