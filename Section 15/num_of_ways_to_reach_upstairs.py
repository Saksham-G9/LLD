from typing import List

def ways_to_reach_upstairs(n: int) -> List[List[int]]:
    def backtrack(remaining: int, path: List[int], result: List[List[int]]):
        if remaining == 0:
            result.append(path.copy())
            return
        if remaining >= 1:
            path.append(1)
            backtrack(remaining - 1, path, result)
            path.pop()
        if remaining >= 2:
            path.append(2)
            backtrack(remaining - 2, path, result)
            path.pop()

    result: List[List[int]] = []
    backtrack(n, [], result)
    return result

result = ways_to_reach_upstairs(5)
for way in result:
    print(way)