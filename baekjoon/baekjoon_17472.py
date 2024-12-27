import sys
from collections import deque
from itertools import combinations


def solution():
    """
    idea: adj array search
        - coloring with bfs
        - backtracking for optimizing the minimum length of total bridges
            - calculate the minimum cost of path of node to node
            - get case by using combinations, selecting the edges such as mst
    feedback:
        - 전체 다리 경로에 섬이 존재 하는가 찾아 줘야 함
    reference:
        - https://www.acmicpc.net/board/view/119531
        - https://www.acmicpc.net/board/view/89137
    """
    # bfs func for coloring each area
    def bfs(y: int, x: int, color: int) -> None:
        q = deque([(y,x)])
        while q:
            vy, vx = q.popleft()
            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < N and -1 < nx < M and grid[ny][nx] == 1:
                    q.append((ny, nx))
                    grid[ny][nx] = color

    # backtrack func for optimizing the total length of bridges
    def dijkstra(start: int, goal: int):
        src_point = area_pos[start]
        for y,x in src_point:
            for s in range(1, max(N, M)):  # bridge size
                for d in range(4):
                    ny, nx = y + dy[d], x + dx[d]
                    if -1 < ny < N and -1 < nx < M and not grid[ny][nx]:
                        nsy, nsx = ny + s*dy[d], nx + s*dx[d]
                        nnsy, nnsx = nsy+dy[d], nsx+dx[d]
                        if -1 < nsy < N and -1 < nsx < M and not grid[nsy][nsx]:
                            if -1 < nnsy < N and -1 < nnsx < M and grid[nnsy][nnsx] == goal:
                                for ns in range(1, s+1):
                                    vny, vnx = ny + ns*dy[d], nx + ns*dx[d]
                                    if grid[vny][vnx]:
                                        break

                                else:
                                    cost[start][goal] = min(cost[start][goal], s+1)
                                    return
        return

    # union-find for find disjoint-set
    def find(x: int):
        if disjoint[x] != x:
            disjoint[x] = find(disjoint[x])
        return disjoint[x]

    def union(y: int, x: int) -> None:
        y = find(y)
        x = find(x)
        if y < x: disjoint[x] = y
        else: disjoint[y] = x

    # get input data
    INF = sys.maxsize
    input = sys.stdin.readline
    N, M = map(int, input().split())
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(map(int, input().split())) for _ in range(N)]

    # do coloring
    num = 2
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                grid[i][j] = num
                bfs(i, j, num)
                num += 1

    # make the shortest path of each node to node, similar to floyd-warshall
    cost = [[INF]*num for _ in range(num)]
    area_pos = {i: [] for i in range(2, num)}
    for i in range(N):
        for j in range(M):
            if grid[i][j]:
                area_pos[grid[i][j]].append((i,j))

    for src in range(2, num):
        for end in range(src+1, num):
            dijkstra(src, end)

    # get combinations of selecting the edge
    answer = INF
    for comb in combinations(combinations(range(2, num),2), num-3):
        flag = 0
        cache = 0
        disjoint = [i for i in range(num)]
        for i,j in comb:
            if find(i) != find(j):
                union(i,j)
            else:
                flag += 1
                break
        if flag:
            continue

        root = 0
        for i in range(2, num):
            if i == disjoint[i]:
                root += 1
            if root > 1:
                break
        if root > 1:
            continue

        for i,j in comb:
            cache += min(cost[i][j], cost[j][i])
        answer = min(answer, cache)

    print(answer) if answer != INF else print(-1)

    # # check current state of grid after coloring
    # for i in range(N):
    #     print(grid[i], end="\n")
    # print()
    #
    # # check current state of cost grid
    # for i in range(num):
    #     print(cost[i], end='\n')

if __name__ == "__main__":
    solution()
