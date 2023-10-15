import sys
from collections import deque
from typing import List


def bfs(y: int, x: int):
    time, flag = -1, False
    q = deque([[y, x]])
    while q:
        for _ in range(len(q)):
            vy, vx = q.popleft()
            if vx+1 >= N or vx+K >= N:
                flag = True
                break
            if graph[vy][vx+1] and not visited[vy][vx+1]:  # 앞으로 한 칸 이동
                q.append([vy, vx+1])
                visited[vy][vx+1] = True

            if vx-1 > time+1 and graph[vy][vx-1] and not visited[vy][vx-1]:  # 뒤로 한 칸 이동, 갈 수 없는 구역을 미리 예상해서 풀어야 함
                q.append([vy, vx-1])
                visited[vy][vx-1] = True

            if graph[(vy+1) % 2][vx+K] and not visited[(vy+1) % 2][vx+K]:  # 앞으로 한 칸 이동
                q.append([(vy+1) % 2, vx+K])
                visited[(vy+1) % 2][vx+K] = True
        time += 1
    return flag


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(2)]
    visited = [[False] * N for _ in range(2)]
    print(1) if bfs(0, 0) else print(0)
