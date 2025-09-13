from abc import ABC, abstractmethod
from enum import Enum, auto


class BreadType(Enum):
    CLASSIC = auto()
    CHEESE = auto()
    PREMIUM = auto()


class GarlicType(Enum):
    NORMAL = auto()
    CHEESE = auto()


class FactoryType(Enum):
    SINGH = auto()
    KING = auto()


# --- Abstract Products ---
class Burger(ABC):
    @abstractmethod
    def create_burger(self): ...


class GarlicBread(ABC):
    @abstractmethod
    def create_garlic_bread(self): ...


# --- Concrete Burgers ---
class ClassicBurger(Burger):
    def create_burger(self):
        print("Creating classic burger")


class CheeseBurger(Burger):
    def create_burger(self):
        print("Creating cheese burger")


class PremiumBurger(Burger):
    def create_burger(self):
        print("Creating premium burger")


class ClassicWheatBurger(Burger):
    def create_burger(self):
        print("Creating wheat classic burger")


class CheeseWheatBurger(Burger):
    def create_burger(self):
        print("Creating wheat cheese burger")


class PremiumWheatBurger(Burger):
    def create_burger(self):
        print("Creating wheat premium burger")


# --- Concrete Garlic Breads ---
class NormalGarlicBread(GarlicBread):
    def create_garlic_bread(self):
        print("Creating normal garlic bread")


class CheeseGarlicBread(GarlicBread):
    def create_garlic_bread(self):
        print("Creating cheese garlic bread")


class NormalWheatGarlicBread(GarlicBread):
    def create_garlic_bread(self):
        print("Creating wheat normal garlic bread")


class CheeseWheatGarlicBread(GarlicBread):
    def create_garlic_bread(self):
        print("Creating wheat cheese garlic bread")


# --- Abstract Factory ---
class ProductFactory(ABC):
    def __init__(self, bread_type: BreadType, garlic_bread_type: GarlicType):
        self.bread_type = bread_type
        self.garlic_bread_type = garlic_bread_type

    @abstractmethod
    def create_burger(self) -> Burger: ...

    @abstractmethod
    def create_garlic_bread(self) -> GarlicBread: ...


# --- Concrete Factories ---
class SinghFactory(ProductFactory):  # Normal bread family
    def create_burger(self):
        match self.bread_type:
            case BreadType.CLASSIC:
                return ClassicBurger()
            case BreadType.CHEESE:
                return CheeseBurger()
            case _:
                return PremiumBurger()

    def create_garlic_bread(self):
        match self.garlic_bread_type:
            case GarlicType.NORMAL:
                return NormalGarlicBread()
            case _:
                return CheeseGarlicBread()


class KingFactory(ProductFactory):  # Wheat bread family
    def create_burger(self):
        match self.bread_type:
            case BreadType.CLASSIC:
                return ClassicWheatBurger()
            case BreadType.CHEESE:
                return CheeseWheatBurger()
            case _:
                return PremiumWheatBurger()

    def create_garlic_bread(self):
        match self.garlic_bread_type:
            case GarlicType.NORMAL:
                return NormalWheatGarlicBread()
            case _:
                return CheeseWheatGarlicBread()


# --- Client Code ---
factory = SinghFactory(BreadType.CHEESE, GarlicType.CHEESE)

burger = factory.create_burger()
garlic_bread = factory.create_garlic_bread()

burger.create_burger()
garlic_bread.create_garlic_bread()
