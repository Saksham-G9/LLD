from abc import ABC, abstractmethod
from enum import Enum, auto


# Entities
class User:
    id: int
    name: str
    cart: "Cart"

    def __init__(self, id: int, name: str):
        print(f"Creating User: id={id}, name={name}")
        self.id = id
        self.name = name


class MenuItems:
    id: int
    name: str
    price: float
    description: str

    def __init__(self, id: int, name: str, price: float, description: str):
        print(f"Creating MenuItem: id={id}, name={name}, price={price}")
        self.id = id
        self.name = name
        self.price = price
        self.description = description


class Location:
    id: int
    name: str
    address: str

    def __init__(self, id: int, name: str, address: str):
        print(f"Creating Location: id={id}, name={name}")
        self.id = id
        self.name = name
        self.address = address


class Restaurent:
    id: int
    name: str
    menuItems: list[MenuItems]
    location: Location

    def __init__(self, id: int, name: str, menuItems: list[MenuItems], location: Location):
        print(f"Creating Restaurent: id={id}, name={name}, location={location.name}")
        self.id = id
        self.name = name
        self.menuItems = menuItems
        self.location = location

    def add(self, item: MenuItems):
        print(f"Adding item {item.name} to restaurant {self.name}")
        self.menuItems.append(item)

    def remove(self, item: MenuItems):
        print(f"Removing item {item.name} from restaurant {self.name}")
        self.menuItems.remove(item)


class Order(ABC):
    id: int
    menuItems: list[MenuItems]
    restaurent: Restaurent
    user: User
    payment: "Payment"
    timing: str

    def __init__(
        self,
        id: int,
        menuItems: list[MenuItems],
        restaurent: Restaurent,
        user: User,
        payment: "Payment",
        timing: str,
    ):
        print(f"Creating Order: id={id}, timing={timing}")
        self.id = id
        self.menuItems = menuItems
        self.restaurent = restaurent
        self.user = user
        self.payment = payment
        self.timing = timing

    def add(self, item: MenuItems):
        print(f"Adding item {item.name} to order {self.id}")
        self.menuItems.append(item)

    def remove(self, item: MenuItems):
        print(f"Removing item {item.name} from order {self.id}")
        self.menuItems.remove(item)

    @abstractmethod
    def create_order(self): ...


class PickupOrder(Order):
    def create_order(self):
        print(f"Pickup order created ({self.timing})")


class DeliveryOrder(Order):
    def create_order(self):
        print(f"Delivery order created ({self.timing})")


class Cart:
    menuItems: list[MenuItems]
    restaurent: Restaurent

    def __init__(self, menuItems: list[MenuItems], restaurent: Restaurent):
        print(f"Creating Cart for restaurant: {restaurent.name}")
        self.menuItems = menuItems
        self.restaurent = restaurent

    def add(self, menuItem: MenuItems):
        print(f"Adding item {menuItem.name} to cart")
        self.menuItems.append(menuItem)

    def remove(self, menuItem: MenuItems):
        print(f"Removing item {menuItem.name} from cart")
        self.menuItems.remove(menuItem)

    def total(self):
        total = 0
        print("Calculating total cart value")
        for item in self.menuItems:
            total += item.price
        return total


# Enum
class OrderFactoryType(Enum):
    PickupOrder = auto()
    DeliveryOrder = auto()


# Managers


class RestaurentManager:
    restaurents: list[Restaurent]

    def __init__(self, restaurents: list[Restaurent]):
        print("Initializing RestaurentManager")
        self.restaurents = restaurents

    def add(self, restaurent: Restaurent) -> None:
        print(f"Adding restaurant {restaurent.name} to manager")
        self.restaurents.append(restaurent)

    def remove(self, restaurent: Restaurent) -> None:
        print(f"Removing restaurant {restaurent.name} from manager")
        self.restaurents.remove(restaurent)
        del restaurent

    def get(self, id: int) -> Restaurent | None:
        print(f"Getting restaurant with id {id}")
        for restaurent in self.restaurents:
            if restaurent.id == id:
                return restaurent
        return None

    def getAll(self) -> list[Restaurent]:
        print("Getting all restaurants")
        return self.restaurents

    def findByLocation(self, location: Location) -> list[Restaurent]:
        print(f"Finding restaurants by location: {location.name}")
        restaurents = []
        for restaurent in self.restaurents:
            if restaurent.location == location:
                restaurents.append(restaurent)
        return restaurents


class OrderManager:
    orders: list[Order]

    def __init__(self, orders: list[Order]):
        print("Initializing OrderManager")
        self.orders = orders

    def add(self, order: Order) -> None:
        print(f"Adding order {order.id} to manager")
        self.orders.append(order)

    def remove(self, order: Order) -> None:
        print(f"Removing order {order.id} from manager")
        self.orders.remove(order)
        del order

    def get(self, id: int) -> Order | None:
        print(f"Getting order with id {id}")
        for order in self.orders:
            if order.id == id:
                return order
        return None

    def getAll(self) -> list[Order]:
        print("Getting all orders")
        return self.orders


# Factory


class OrderFactory(ABC):
    @abstractmethod
    def create_order(
        self,
        type: OrderFactoryType,
        id: int,
        menuItems: list[MenuItems],
        restaurent: Restaurent,
        user: User,
        payment: "Payment",
    ) -> Order: ...


class ScheduleOrderFactory(OrderFactory):
    def create_order(
        self,
        type: OrderFactoryType,
        id: int,
        menuItems: list[MenuItems],
        restaurent: Restaurent,
        user: User,
        payment: "Payment",
    ):
        print(f"Creating a scheduled order of type: {type.name}")
        timing = "Scheduled"
        match type:
            case OrderFactoryType.PickupOrder:
                return PickupOrder(id, menuItems, restaurent, user, payment, timing)
            case OrderFactoryType.DeliveryOrder:
                return DeliveryOrder(id, menuItems, restaurent, user, payment, timing)
            case _:
                raise ValueError("Invalid order type")


class OrderNowFactory(OrderFactory):
    def create_order(
        self,
        type: OrderFactoryType,
        id: int,
        menuItems: list[MenuItems],
        restaurent: Restaurent,
        user: User,
        payment: "Payment",
    ):
        print(f"Creating an order for now of type: {type.name}")
        timing = "Now"
        match type:
            case OrderFactoryType.PickupOrder:
                return PickupOrder(id, menuItems, restaurent, user, payment, timing)
            case OrderFactoryType.DeliveryOrder:
                return DeliveryOrder(id, menuItems, restaurent, user, payment, timing)
            case _:
                raise ValueError("Invalid order type")


# Payment
class Payment(ABC):
    @abstractmethod
    def pay(self):
        ... # Corrected from '...' to '...'


class PayWithUPI(Payment):
    def pay(self):
        print("Paid with UPI")


class PayWithCard(Payment):
    def pay(self):
        print("Paid with Card")


class PayWithNetBanking(Payment):
    def pay(self):
        print("Paid with Net Banking")


class ZomatoApp:
    def __init__(self):
        print("--- Initializing Zomato Simulation ---")
        self.setup()

    def setup(self):
        # Create Locations
        print("\n--- Creating Locations ---")
        self.location1 = Location(1, "New York", "123 Main St")
        self.location2 = Location(2, "London", "456 Baker St")

        # Create Menu Items
        print("\n--- Creating Menu Items ---")
        self.item1 = MenuItems(1, "Burger", 150, "A delicious burger")
        self.item2 = MenuItems(2, "Pizza", 300, "Cheesy pizza")
        self.item3 = MenuItems(3, "Fries", 80, "Crispy fries")
        self.item4 = MenuItems(4, "Pasta", 250, "Creamy pasta")

        # Create Restaurants
        print("\n--- Creating Restaurants ---")
        restaurant1 = Restaurent(1, "Food Palace", [self.item1, self.item2], self.location1)
        restaurant2 = Restaurent(2, "Pizza Hub", [self.item2, self.item4], self.location1)
        restaurant3 = Restaurent(3, "Burger Queen", [self.item1, self.item3], self.location2)

        # Create a Restaurant Manager
        print("\n--- Creating a Restaurant Manager ---")
        self.restaurant_manager = RestaurentManager([restaurant1, restaurant2, restaurant3])

    def run(self):
        print("\n--- Starting Zomato Simulation ---")

        # Create a User
        print("\n--- Creating a User ---")
        user = User(1, "John Doe")

        # User searches for restaurants in a location
        print(f"\n--- User searching for restaurants in {self.location1.name} ---")
        restaurants_in_location = self.restaurant_manager.findByLocation(self.location1)
        print(f"Found {len(restaurants_in_location)} restaurants:")
        for r in restaurants_in_location:
            print(f"- {r.name}")

        # User chooses a restaurant
        chosen_restaurant = restaurants_in_location[0]
        print(f"\n--- User chose {chosen_restaurant.name} ---")

        # User creates a cart and adds items
        print("\n--- User creates a cart and adds items ---")
        cart = Cart([], chosen_restaurant)
        user.cart = cart
        user.cart.add(self.item1)
        user.cart.add(self.item2)

        print(f"Total cart value: {user.cart.total()}")

        # User chooses a payment method
        print("\n--- User chooses a payment method ---")
        payment_method = PayWithUPI()

        # Create an order using a factory
        print("\n--- Creating an order using a factory ---")
        order_factory = OrderNowFactory()
        order = order_factory.create_order(
            OrderFactoryType.DeliveryOrder,
            1,
            user.cart.menuItems,
            chosen_restaurant,
            user,
            payment_method,
        )

        # Create an Order Manager
        print("\n--- Creating an Order Manager ---")
        order_manager = OrderManager([])
        order_manager.add(order)

        # Process the order
        print("\n--- Processing the order ---")
        order.create_order()
        order.payment.pay()

        print(f"\nOrder Type: {order.timing}")

        print(f"\n--- {chosen_restaurant.name}'s Menu ---")
        for item in chosen_restaurant.menuItems:
            print(f"{item.name}: {item.price}")

        print("\n--- User's Order ---")
        for item in order.menuItems:
            print(f"{item.name}")

        print("\n--- Zomato Simulation Finished ---")


if __name__ == "__main__":
    app = ZomatoApp()
    app.run()