import sys
from collections import deque, defaultdict


def solution():
    """
    idea1: floyd-warshall with unioin-find
        - 시간 복잡도가 N**3까지 가능해서, 플루이드 워셜 쓰는게 더 편해 보임
    feedback1:
        - 사이클 생기면 -1 출력해야 해서, 플루이드 워셜은 사용 불가 (사이클 못잡음)
        - 유니온 파인드로 걸러버리면 가능할 듯
        - 만약 1번 도시에서 출발해 어떤 도시로 가는 과정에서 시간을 무한히 오래 전으로 되돌릴 수 있다면 첫째 줄에 -1을 출력한다
        => 위 조건 때문에 벨만 포드를 쓰는게 맞다

    """
    def find(x: int) -> int:
        if arr[x] != x:
            arr[x] = find(arr[x])
        return arr[x]

    def union(y: int, x: int) -> None:
        y = find(y)
        x = find(x)

        if x > y: arr[x] = y
        else: arr[y] = x

    # init the data structure
    INF = sys.maxsize
    input = sys.stdin.readline
    N, M = map(int, input().split())

    arr = [i for i in range(N+1)]
    grid = [[INF] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        s, e, c = map(int, input().split())
        grid[s][e] = c
        if find(s) != find(e):
            union(s, e)
        else:
            print(-1)
            return

    # floyd-warshall
    for k in range(1, N+1):
        for y in range(1, N+1):
            for x in range(1, N+1):
                if y != x:
                    grid[y][x] = min(grid[y][x], grid[y][k] + grid[k][x])

    # check the grid
    for i in range(N+1):
        print(grid[i], end='\n')


def solution2():
    """
    idea: bellman-ford

    feedback:
        - 1로부터 경로가 없는 친구들은 -1 출력하게 만들라는데

    reference:
        https://www.acmicpc.net/board/view/131713
    """
    # bellman-ford func
    def bellman_ford(src: int):
        cost[src] = 0
        for k in range(N):
            for i in range(1, N+1):
                for nx, nc in graph[i]:
                    new_cost = cost[i] + nc
                    if new_cost < cost[nx]:
                        cost[nx] = new_cost
                        if k == N-1:
                            return True
        return False

    # init the data structure
    INF = 1e+9
    input = sys.stdin.readline
    N, M = map(int, input().split())

    cost = [INF]*(N+1)
    graph = defaultdict(list)
    cache = set()
    for _ in range(M):
        s, e, c = map(int, input().split())
        graph[s].append((e, c))
        if s == 1:
            cache.add(e)

    if cache and bellman_ford(1):
        print(-1)

    else:
        for i in range(2, N+1):
            print(cost[i] if cost[i] != INF else -1, end="\n")


if __name__ == "__main__":
    solution2()
