import sys
from collections import deque, defaultdict
from typing import List


def solution():
    N, L, R = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

    def calculate(nums: int, populations: int, unions: int, visited: List[List], graph: List[List]):
        cnt = int(populations / unions)
        for r in range(N):
            for c in range(N):
                if visited[r][c] == nums:
                    graph[r][c] = cnt

    def union_find(y: int, x: int, nums: int, visited: List[List], graph: List[List]):
        populations, unions = graph[y][x], 1
        visited[y][x] = nums
        q = deque([(y, x)])
        while q:
            vy, vx = q.popleft()
            for i in range(4):
                ny, nx = dy[i] + vy, dx[i] + vx
                if -1 < ny < N and -1 < nx < N and not visited[ny][nx]:
                    cnt = abs(graph[vy][vx] - graph[ny][nx])
                    if L <= cnt <= R:
                        unions += 1
                        visited[ny][nx] = nums
                        populations += graph[ny][nx]
                        q.append((ny, nx))

        return populations, unions

    result = 0
    while True:
        visit = [[0] * N for _ in range(N)]
        k, moving = 1, defaultdict(list)
        for r in range(N):
            for c in range(N):
                if not visit[r][c]:
                    population, union = union_find(r, c, k, visit, grid)
                    if union > 1:
                        moving[k].append(population), moving[k].append(union)
                        k += 1
                    else:  # 일단 한 번은 무조건 탐색을 들어가기 때문에, 연합이 아닌 애들은 다시 미방문 처리 필요
                        visit[r][c] = 0

        for key in moving.keys():
            population, union = moving[key]
            calculate(key, population, union, visit, grid)

        if not len(moving):
            break
        result += 1

    print(result)


if __name__ == "__main__":
    solution()
