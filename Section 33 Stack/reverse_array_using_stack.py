def reverse_array_using_stack(arr, n):
    # TODO: Implement this function
    stack = []

    for el in arr:
        stack.append(el)
    for i in range(len(arr)):
        arr[i] = stack.pop()
    return arr


arr = [1, 2, 3, 4, 5]

n = 5
print(reverse_array_using_stack(arr, n))
