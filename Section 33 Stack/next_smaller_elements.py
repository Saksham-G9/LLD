def next_smaller_elements(arr: list[int]):
    stack = []
    res = [-1] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        el = arr[i]

        while stack and stack[-1] > el:
            stack.pop()

        if stack:
            res[i] = stack[-1]

        stack.append(el)

    return res

arr = [4, 5, 2, 10, 8]
print(next_smaller_elements(arr))