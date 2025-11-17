def power(a: int, n: int) -> float:
    if n == 1:
        return a

    temp = n // 2

    left_part = power(a, temp)
    right_part = power(a, n - temp)

    return left_part * right_part


def power2(a, b):
    res = 1

    while b:
        if b % 2 == 0:
            a *= a
        else:
            res *= a
        b //= 2

    return a * res


print(power(2, 10))
