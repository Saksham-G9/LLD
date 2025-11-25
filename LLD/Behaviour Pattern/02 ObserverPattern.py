from abc import ABC, abstractmethod
from typing import Optional


class IObserver(ABC):
    def __init__(self, channel: Optional["IChannel"] = None):

        self.channel = channel

    @abstractmethod
    def update(self) -> None: ...


class IChannel(ABC):

    def __init__(self, name: str):
        self._channel_name = name
        self.observers: list[IObserver] = []

        self._latest_video: Optional[str] = None

    @abstractmethod
    def upload_video(self, text: str) -> None:
        pass

    @abstractmethod
    def add(self, observer: IObserver) -> None: ...

    @abstractmethod
    def remove(self, observer: IObserver) -> None: ...

    @abstractmethod
    def notify(self) -> None: ...


class Channel(IChannel):

    def upload_video(self, text: str) -> None:
        self._latest_video = text
        self.notify()

    def add(self, observer: IObserver) -> None:
        if observer not in self.observers:

            observer.channel = self
            self.observers.append(observer)

    def remove(self, observer: IObserver) -> None:
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self) -> None:

        for observer in tuple(self.observers):
            observer.update()

    def get_latest_video(self) -> Optional[str]:
        return self._latest_video

    def get_channel_name(self) -> str:
        return self._channel_name


class Subscriber(IObserver):
    def update(self) -> None:
        video = self.channel.get_latest_video()
        channel_name = self.channel.get_channel_name()
        print(f"Video uploaded by title {video} by {channel_name}")


if __name__ == "__main__":
    channel = Channel("Channel 1")

    sub1 = Subscriber()
    channel.add(sub1)

    sub2 = Subscriber()
    channel.add(sub2)

    sub3 = Subscriber()
    channel.add(sub3)

    channel.upload_video("Hello there!")
