def factorial(num: int) -> int:
    # Base Case
    if num == 1:
        return 1
    # Recursion Call
    return num * factorial(num - 1)


def fact(n: int) -> int:
    res = 1

    for i in range(2, n + 1):
        res *= i
    return res


n = 5
result = fact(n)
print(f"Factorial of num {n} is {result}")
