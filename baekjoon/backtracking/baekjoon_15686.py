import sys
from itertools import combinations

# def combinations(n: int, k: int):
#     """ """
#     result, curr = [], []
#
#     def backtracking(src: int, count: int):
#         if count == 0:
#             result.append(curr[:])
#             return
#
#         for i in range(src, n+1):
#             curr.append(i)
#             backtracking(i+1, count-1)
#             curr.pop()
#
#     backtracking(1, k)
#     return result


N, M = map(int, sys.stdin.readline().split())
grid, house, chicken = [], set(), set()

for i in range(N):
    col = list(map(int, sys.stdin.readline().split()))
    grid.append(col)
    for j in range(N):
        if col[j] == 1:
            house.add((i, j))
        elif col[j] == 2:
            chicken.add((i, j))

result = float('inf')
for sub in set(combinations(chicken, M)):
    save = set(sub)
    remove = chicken - save
    for i, j in remove:
        grid[i][j] = 0

    total = 0
    for r, c in house:
        tmp_distance = float('inf')
        for i, j in save:
            tmp_distance = min(abs(r - i) + abs(c - j), tmp_distance)  # update
        total += tmp_distance
    result = min(result, total)

    for i, j in remove:
        grid[i][j] = 1
print(result)
