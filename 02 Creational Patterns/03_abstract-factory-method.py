from abc import ABC, abstractmethod
from enum import Enum, auto


class BreadType(Enum):
    BASIC = auto()
    CHEESE = auto()
    PREMIUM = auto()


class GarlicType(Enum):
    NORMAL = auto()
    CHEESE = auto()


class FactoryType(Enum):
    SINGHFACTORY = auto()
    KINGFACTORY = auto()


class Burger(ABC):
    @abstractmethod
    def create_burger(self): ...


class GarlicBread(ABC):
    @abstractmethod
    def create_garlic_bread(self): ...


class ClassicBurger(Burger):
    def create_burger(self):
        print("Creating simple classic burger")


class CheeseBurger(Burger):
    def create_burger(self):
        print("Creating simple cheese burger")


class PremiumBurger(Burger):
    def create_burger(self):
        print("Creating simple premium burger")


class ClassicWheatBuger(Burger):
    def create_burger(self):
        print("Creating wheat classic burger")


class CheeseWheatBurger(Burger):
    def create_burger(self):
        print("Creating wheat cheese burger")


class PremiumWheatBurger(Burger):
    def create_burger(self):
        print("Creating wheat premium burger")


class ProductFactory(ABC):
    def __init__(self, bread_type: BreadType, garlic_bread_type: GarlicType):
        self.bread_type = bread_type
        self.garlic_bread_type = garlic_bread_type

    @abstractmethod
    def create_burger(self): ...


class NormalGarlicBread(GarlicBread):
    def create_garlic_bread(self):
        print("Creating normal garlic bread")


class CheeseGarlicBread(GarlicBread):
    def create_garlic_bread(self):
        print("Creating cheese garlic bread")


class NormalWheatGarlicBread(GarlicBread):
    def create_garlic_bread(self):
        print("Creating normal wheat garlic bread")


class CheeseWheatGarlicBread(GarlicBread):
    def create_garlic_bread(self):
        print("Creating cheese wheat garlic bread")


class KingFactory(ProductFactory):
    def create_burger(self):
        match self.bread_type:
            case BreadType.BASIC:
                self.burger = ClassicBurger()
            case BreadType.CHEESE:
                self.burger = CheeseBurger()
            case _:
                self.burger = PremiumBurger()

        self.burger.create_burger()

    def create_garlic_bread(self):
        match self.garlic_bread_type:
            case GarlicType.NORMAL:
                self.garlic_bread = NormalGarlicBread()
            case _:
                self.garlic_bread = CheeseGarlicBread()
        self.garlic_bread.create_garlic_bread()


class SinghFactory(ProductFactory):
    def create_burger(self):
        match self.bread_type:
            case BreadType.BASIC:
                self.burger = ClassicWheatBuger()
            case BreadType.CHEESE:
                self.burger = CheeseWheatBurger()
            case _:
                self.burger = PremiumWheatBurger()

        self.burger.create_burger()

    def create_garlic_bread(self):
        match self.garlic_bread_type:
            case GarlicType.NORMAL:
                self.garlic_bread = NormalWheatGarlicBread()
            case _:
                self.garlic_bread = CheeseWheatGarlicBread()

        self.garlic_bread.create_garlic_bread()


factory = SinghFactory(BreadType.BASIC, GarlicType.NORMAL)
factory.create_burger()
factory.create_garlic_bread()
