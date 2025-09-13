class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def __init__(self, value):
        if not hasattr(self, "_initialized"):
            self.value = value
            self._initialized = True
            print(f"Initializing instance with value: {self.value}")
        else:
            print(f"Instance already initialized. Value remains: {self.value}")

# Create the first instance
s1 = Logger("first_value")

# Create a second instance. __new__ returns the same object,
# and __init__ recognizes it has already been initialized.
s2 = Logger("second_value")

print(f"\ns1 is s2: {s1 is s2}")
print(f"s1.value: {s1.value}")
print(f"s2.value: {s2.value}")