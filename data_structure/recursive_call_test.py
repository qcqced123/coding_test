from typing import List

""" 
function args which is mutable object states are in-place
function args which is immutable object states are out-of-place 
"""


def dfs(x: int, visit: List, weight: int):
    print(visit)
    print(weight)
    if x == N-1:
        return
    visit[x] = True
    dfs(x+1, visit, weight+1)
    print(f"after visit list: {visit}")
    print(f"after weight: {weight}")


N = 4
visited = [False] * N
graph = list(range(N))
dfs(0, visited, 0)

print(visited)
