from abc import ABC, abstractmethod


class ICommand(ABC):
    @abstractmethod
    def execute(self, state: bool): ...


class Applience(ABC):
    @abstractmethod
    def on(self): ...
    @abstractmethod
    def off(self): ...


class Light(Applience):
    def on(self):
        print("Light is ON!")

    def off(self):
        print("Light is OFF!")


class AC(Applience):
    def on(self):
        print("AC is ON!")

    def off(self):
        print("AC is OFF!")


class ConcreteCommand(ICommand):
    def __init__(self, applience: Applience):
        self.applience = applience

    def execute(self, state: bool):
        if state:
            self.applience.on()
        else:
            self.applience.off()


class RemoteControl:
    def __init__(self):
        self._commands: list[ICommand] = []
        self._state: list[bool] = []

    def setCommand(self, command: ICommand):
        self._commands.append(command)
        self._state.append(False)

    def pressButton(self, idx: int):
        self._state[idx] = not self._state[idx]
        self._commands[idx].execute(self._state[idx])


light = ConcreteCommand(Light())
ac = ConcreteCommand(AC())

remoteControl = RemoteControl()
remoteControl.setCommand(light)
remoteControl.setCommand(ac)

remoteControl.pressButton(0)
remoteControl.pressButton(1)
remoteControl.pressButton(0)
remoteControl.pressButton(1)