from collections import deque


def find_winner(n, k):
    arr = [i for i in range(1, n + 1)]  # O(N)

    i = 0
    while len(arr) > 1:
        i = (i + k - 1) % len(arr)
        arr.pop(i)  # O(n)
    return arr[0]


def find_winner2(n, k):
    dq = deque(range(1, n + 1))

    while len(dq) > 1:
        for _ in range(k - 1):
            el = dq.popleft()
            dq.append(el)
        dq.popleft()

    return dq[0]


print(find_winner2(6, 5))
