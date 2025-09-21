from abc import ABC, abstractmethod
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


# Interfaces
class INotification(ABC):
    @abstractmethod
    def notify(self, message: "NotificationMessage"): ...


class INotificationDecorator(INotification):
    def __init__(self, wrapped: INotification):
        self._wrapped = wrapped


class ILogger(ABC):
    @abstractmethod
    def logger(self, message: str): ...


class IPersistence(ABC):
    @abstractmethod
    def save(self, data: str): ...


# Message Class
class NotificationMessage:
    def __init__(self, content: str):
        self.content = content


# Implementations
class SMSNotification(INotification):
    def notify(self, message: NotificationMessage):
        return f"SMS: {message.content}"


class PopupNotification(INotification):
    def notify(self, message: NotificationMessage):
        return f"Popup: {message.content}"


class WhatsAppNotification(INotification):
    def notify(self, message: NotificationMessage):
        return f"WhatsApp: {message.content}"


# Decorators
class SignatureNotificationDecorator(INotificationDecorator):
    def __init__(self, wrapped: INotification, signature: str):
        super().__init__(wrapped)
        self._signature = signature

    def notify(self, message: NotificationMessage):
        base_message = self._wrapped.notify(message)
        return f"{base_message}\n\n-- {self._signature}"


class HeaderDecorator(INotificationDecorator):
    def __init__(self, wrapped: INotification, header: str):
        super().__init__(wrapped)
        self._header = header

    def notify(self, message: NotificationMessage):
        base_message = self._wrapped.notify(message)
        return f"{self._header}\n{base_message}"


# Logger & Persistence
class ConsoleLog(ILogger):
    def logger(self, message: str):
        logging.info(f"Sending notification: {message}")


class SQLStorage(IPersistence):
    def save(self, data: str):
        print(f"Storing in SQL DB: {data}")


# Manager
class NotificationManager:
    def __init__(self, logger: ILogger, persistence: IPersistence):
        self._notifications: list[INotification] = []
        self._logger = logger
        self._persistence = persistence

    def add_notification(self, notification: INotification):
        self._notifications.append(notification)

    def remove_notification(self, notification: INotification):
        if notification in self._notifications:
            self._notifications.remove(notification)

    def notify_all(self, message: NotificationMessage):
        for notif in self._notifications:
            self._logger.logger(message.content)
            result = notif.notify(message)
            print(result)
            self._persistence.save(result)


# Usage
if __name__ == "__main__":
    logger = ConsoleLog()
    persistence = SQLStorage()

    sms = SMSNotification()
    sms_with_signature = SignatureNotificationDecorator(sms, "Saksham Gupta")
    header_sms = HeaderDecorator(sms_with_signature, "Important Notice:")

    manager = NotificationManager(logger, persistence)
    manager.add_notification(header_sms)

    msg = NotificationMessage("Order Placed")
    manager.notify_all(msg)
