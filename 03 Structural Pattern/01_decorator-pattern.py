import functools
import time


def logging_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling '{func.__name__}' with args={args} and kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"'{func.__name__}' returned: {result} ")

    return wrapper


@logging_decorator
def complex_function(a, b):
    print("Excecuting complex function...")
    time.sleep(1)
    return a * b


complex_function(4,5)