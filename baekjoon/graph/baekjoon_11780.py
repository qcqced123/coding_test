import sys
from collections import defaultdict


def solution():
    """ 도시 to 도시 최소 비용 출력
    idea: floyd-warshall
        - question 1:
            - 버스 == 간선
            - 유향 그래프, 양의 간선값, 도시 to 도시 사이 간선이 여러개 가능(가장 작은거로 초기화)
            - grid 자체 출력하면 될 듯

        - question 2:
            - 자료구조: 해시 이용
                - key: node to node 경로
                - value: 경로에 포함된 노드
    """
    # get input data
    INF = sys.maxsize
    input = sys.stdin.readline
    N = int(input())  # number of nodes
    M = int(input())  # number of edges
    grid = [[INF]*N for _ in range(N)]

    # init grid with connected information
    cache = defaultdict(list)
    for _ in range(M):
        src, end, cost = map(int, input().split())
        if cost < grid[src-1][end-1]:
            cache[(src, end)] = [src, end]
            grid[src-1][end-1] = cost

    # do update the grid with floyd-warshall
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i != j:
                    vc = grid[i][j]
                    nc = grid[i][k]+grid[k][j]
                    if nc < vc:
                        grid[i][j] = nc
                        cache[(i+1,j+1)] = cache[(i+1,k+1)] + cache[(k+1,j+1)][1:]
                else:
                    grid[i][j] = 0

    # answering the question 1: printing the minimum cost of each node to node
    for i in range(N):
        for j in range(N):
            if grid[i][j] == INF: grid[i][j] = 0

    for i in range(N):
        print(*grid[i], end="\n")

    # answering the question 2: printing the number and path of shortest path of each node to node
    for i in range(N):
        for j in range(N):
            if grid[i][j]: print(len(cache[(i+1,j+1)]), *cache[(i+1,j+1)])
            else: print(0)


if __name__ == "__main__":
    solution()
