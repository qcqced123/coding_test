from typing import List


def dfs(x: int, visit: List):
    print(visit)
    if x == N-1:
        return
    visit[x] = True
    dfs(x+1, visit)
    visit[x] = False  # 이렇게 하면 다시 재활용 가능


N = 4
visited = [False] * N
graph = list(range(N))
dfs(0, visited)

print(visited)
