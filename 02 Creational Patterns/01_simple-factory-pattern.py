from abc import ABC, abstractmethod
from enum import Enum, auto


class BugerType(Enum):
    BASIC = auto()
    CHEESE = auto()
    PREMIUM = auto()


class Burger(ABC):
    @abstractmethod
    def create_burger(self): ...


class ClassicBuger(Burger):
    def create_burger(self):
        print("Creating classic burger")


class CheeseBurger(Burger):
    def create_burger(self):
        print("Creating cheese burger")


class PremiumBurger(Burger):
    def create_burger(self):
        print("Creating premium burger")


class BurgerFactory:

    def __init__(self, type: BugerType):
        self.type = type
        match type:
            case BugerType.BASIC:
                self.burger = ClassicBuger()
            case BugerType.CHEESE:
                self.burger = CheeseBurger()
            case _:
                self.burger = PremiumBurger()

    def create_burger(self):
        self.burger.create_burger()


if __name__ == "__main__":
    burger_factory = BurgerFactory(BugerType.PREMIUM)
    burger_factory.create_burger()
