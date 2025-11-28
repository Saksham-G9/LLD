arr = [7, 1, 5, 3, 6, 4, 15]

# max_arr = float("-inf")

# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         max_arr = max(max_arr, arr[j] - arr[i])

# print(max_arr)

curr_min, max_profit = arr[0], float("-inf")

for el in arr[1:]:
    curr_min = min(el, curr_min)
    max_profit = max(max_profit, el)

print(max_profit)



