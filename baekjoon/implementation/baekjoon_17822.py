import sys
from typing import List
from collections import deque
"""
[풀이]
** 인덱스 안맞는거 조심
1) rotate
    - select for rotate
    - rotate
2) Remove
    - 원판 내부에서 인접 처리
    - 원판 끼리의 인접 처리
3) Count
"""


def rotate(x: int, d: int, k: int, graph: List[List[int]]):
    q = deque()
    q.extend(graph[x])
    if d == 0:
        q.rotate(k)
    else:
        q.rotate(-k)
    graph[x] = list(q)


def change_avg(n: int, m: int, graph: List[List[int]]):
    avg_count = 0
    all_sum = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                avg_count += 1
                all_sum += graph[i][j]
    if avg_count == 0:
        return False
    avg = all_sum / avg_count
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                if graph[i][j] > avg:
                    graph[i][j] -= 1
                elif graph[i][j] < avg:
                    graph[i][j] += 1
    return True


def dfs(x: int, y: int, n: int, m: int, visited: List[List[int]], graph: List[List[int]]):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    value = graph[x][y]
    graph[x][y] = 0
    count = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > ny or ny >= m:
                if y == 0:
                    ny = m-1
                elif y == m-1:
                    ny = 0
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]:
                    if graph[nx][ny] == value:
                        count += 1
                        graph[nx][ny] = 0
                        visited[nx][ny] = True
                        q.append((nx, ny))
    if count == 0:
        graph[x][y] = value
    return count


def solution():
    n, m, t = map(int, sys.stdin.readline().split())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    for _ in range(t):
        x, d, k = map(int, sys.stdin.readline().split())
        check_sum = 0
        for i in range(n):
            check_sum += sum(graph[i])
            if (i+1) % x == 0:  # select for rotate
                rotate(i, d, k, graph)
        if check_sum == 0:
            break
        else:
            visited = [[False] * m for _ in range(n)]
            count = 0
            for i in range(n):
                for j in range(m):
                    if not visited[i][j] and graph[i][j] != 0:
                        count += dfs(i, j, n, m, visited, graph)
            if count == 0:
                change_avg(n, m, graph)

    answer = 0
    for i in range(n):
        answer += sum(graph[i])
    print(answer)


if __name__ == "__main__":
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    solution()
