from abc import ABC, abstractmethod
from typing import List, Set
from weakref import WeakSet
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class IChannel(ABC):
    """Abstract base class for observable channels"""

    def __init__(self, name: str):
        if not name:
            raise ValueError("Channel name cannot be empty")
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @abstractmethod
    def subscribe(self, subscriber: "IObserver") -> bool: ...

    @abstractmethod
    def unsubscribe(self, subscriber: "IObserver") -> bool: ...

    @abstractmethod
    def notify(self, video_title: str) -> None: ...

    @abstractmethod
    def upload(self, title: str) -> None: ...

    @abstractmethod
    def get_latest_video(self) -> str: ...

    @abstractmethod
    def get_subscriber_count(self) -> int: ...

    def __str__(self) -> str:
        return self._name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self._name}')"


class IObserver(ABC):
    """Abstract base class for observers"""

    def __init__(self, name: str):
        if not name:
            raise ValueError("Observer name cannot be empty")
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @abstractmethod
    def update(self, channel: IChannel, video_title: str) -> None: ...

    def __str__(self) -> str:
        return self._name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self._name}')"

    def __eq__(self, other) -> bool:
        if not isinstance(other, IObserver):
            return False
        return self._name == other._name

    def __hash__(self) -> int:
        return hash(self._name)


class YoutubeChannel(IChannel):
    """Concrete implementation of a YouTube channel using Observer pattern"""

    def __init__(self, name: str):
        super().__init__(name)
        self._subscribers: Set[IObserver] = set()  # Use set for O(1) lookups
        self._latest_video = ""
        self._video_count = 0

    def subscribe(self, subscriber: IObserver) -> bool:
        """Subscribe a subscriber to this channel"""
        if not isinstance(subscriber, IObserver):
            raise TypeError("Subscriber must implement IObserver interface")

        if subscriber in self._subscribers:
            logger.info(f"{subscriber} is already subscribed to {self}")
            return False

        self._subscribers.add(subscriber)
        logger.info(f"{subscriber} subscribed to {self}")
        return True

    def unsubscribe(self, subscriber: IObserver) -> bool:
        """Unsubscribe a subscriber from this channel"""
        if not isinstance(subscriber, IObserver):
            raise TypeError("Subscriber must implement IObserver interface")

        if subscriber not in self._subscribers:
            logger.warning(f"{subscriber} is not subscribed to {self}")
            return False

        self._subscribers.remove(subscriber)
        logger.info(f"{subscriber} unsubscribed from {self}")
        return True

    def notify(self, video_title: str) -> None:
        """Notify all subscribers about new content"""
        logger.info(
            f"Notifying {len(self._subscribers)} subscribers about '{video_title}'"
        )
        for (
            subscriber
        ) in (
            self._subscribers.copy()
        ):  # Use copy to avoid modification during iteration
            try:
                subscriber.update(self, video_title)
            except Exception as e:
                logger.error(f"Error notifying {subscriber}: {e}")

    def upload(self, title: str) -> None:
        """Upload a new video and notify subscribers"""
        if not title:
            raise ValueError("Video title cannot be empty")

        self._latest_video = title
        self._video_count += 1
        logger.info(f"Uploaded video: '{title}' to {self}")
        self.notify(title)

    def get_latest_video(self) -> str:
        return self._latest_video

    def get_subscriber_count(self) -> int:
        return len(self._subscribers)

    def get_subscribers(self) -> List[IObserver]:
        """Return a list of current subscribers"""
        return list(self._subscribers)


class Subscriber(IObserver):
    """Concrete implementation of a subscriber"""

    def __init__(self, name: str):
        super().__init__(name)
        self._watched_videos: List[tuple[str, str]] = []  # (channel_name, video_title)

    def update(self, channel: IChannel, video_title: str) -> None:
        """Receive notification about new video"""
        self._watched_videos.append((str(channel), video_title))
        print(f"📧 Hi {self.name}! New video uploaded by {channel}: '{video_title}'")

    def get_watched_videos(self) -> List[tuple[str, str]]:
        """Get list of videos this subscriber has been notified about"""
        return self._watched_videos.copy()

    def get_notification_count(self) -> int:
        """Get total number of notifications received"""
        return len(self._watched_videos)


# Memory-efficient version using Weak References
class WeakYoutubeChannel(YoutubeChannel):
    """Memory-efficient version that uses weak references to avoid memory leaks"""

    def __init__(self, name: str):
        super().__init__(name)
        self._subscribers = (
            WeakSet()
        )  # Automatically removes subscribers when they're garbage collected


# Thread-safe version (if needed)
import threading


class ThreadSafeYoutubeChannel(YoutubeChannel):
    """Thread-safe version of YouTube channel"""

    def __init__(self, name: str):
        super().__init__(name)
        self._lock = threading.RLock()

    def subscribe(self, subscriber: IObserver) -> bool:
        with self._lock:
            return super().subscribe(subscriber)

    def unsubscribe(self, subscriber: IObserver) -> bool:
        with self._lock:
            return super().unsubscribe(subscriber)

    def notify(self, video_title: str) -> None:
        with self._lock:
            super().notify(video_title)

    def upload(self, title: str) -> None:
        with self._lock:
            super().upload(title)


# Enhanced client code with demonstrations
def demonstrate_observer_pattern():
    """Demonstrate various features of the observer pattern"""

    print("=== Observer Pattern Demonstration ===\n")

    # Create channels
    channel_1 = YoutubeChannel("Tech Reviews")
    channel_2 = YoutubeChannel("Cooking Tutorials")

    # Create subscribers
    sub1 = Subscriber("Alice")
    sub2 = Subscriber("Bob")
    sub3 = Subscriber("Charlie")

    # Subscribe subscribers to channels
    print("1. Subscribing users:")
    channel_1.subscribe(sub1)
    channel_1.subscribe(sub2)
    channel_1.subscribe(sub3)
    channel_2.subscribe(sub2)
    channel_2.subscribe(sub3)

    print(f"\n{channel_1} has {channel_1.get_subscriber_count()} subscribers")
    print(f"{channel_2} has {channel_2.get_subscriber_count()} subscribers\n")

    # Upload videos
    print("2. Uploading videos:")
    channel_1.upload("Python Design Patterns")
    channel_2.upload("5-minute Pasta Recipe")

    # Unsubscribe and upload again
    print("\n3. Unsubscribing Bob from Tech Reviews:")
    channel_1.unsubscribe(sub2)

    print(f"\n{channel_1} now has {channel_1.get_subscriber_count()} subscribers")
    channel_1.upload("Advanced Python Tips")

    # Show subscriber history
    print("\n4. Subscriber notification history:")
    for sub in [sub1, sub2, sub3]:
        print(f"{sub} received {sub.get_notification_count()} notifications")


if __name__ == "__main__":
    demonstrate_observer_pattern()
