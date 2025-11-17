def fib(n: int, a=0, b=1) -> None:
    if n == 0:
        print()
        return
    print(a, end=" ")

    return fib(n - 1, b, a + b)


# Driver code
n = 10
fib(n)
