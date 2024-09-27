import sys
import heapq
from collections import deque


def solution():
    """ 어릴 때 해봤던 그 추억의 보드게임
    최소 횟수로 도착점 도착 (최대한 빠르게 허들)

    [격자]
    1 ... 10 11 12 ... 20 ... 100
    l

    idea: bfs with conditional moving
        1) direction 정의
        2) 배열 초기화
            - 배열의 원소: 도착지를 원소값으로 설정

    Question 1. 굳이 방문처리를 해야할까??
        - 할거면, 사다리 & 뱀 도착 위치에는 하면 안될듯
    """
    def is_valid(x):
        return 0 < x < 101 and visited[x] != -1

    def priority_bfs():
        h = []
        heapq.heappush(h, (0, 1))
        while h:
            vc, vx = heapq.heappop(h)
            for i in range(6):
                nx = vx + dx[i]
                if nx == 100:
                    return vc + 1

                if is_valid(nx):
                    if arr[nx]:
                        nx = arr[nx]

                    heapq.heappush(h, (vc+1, nx))
        return

    def bfs():
        q = deque([(1, 0)])  # position, count
        visited[1] = -1
        while q:
            vx, vc = q.popleft()
            for i in range(6):
                nx = vx + dx[i]
                if nx == 100:
                    return vc + 1

                if is_valid(nx):
                    if arr[nx]:
                        nx = arr[nx]
                    else:
                        visited[nx] = -1
                    q.append((nx, vc+1))

    N, M = map(int, sys.stdin.readline().split())

    arr = [0]*102
    visited = [0]*102
    blocks = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N+M)]

    dx = (1, 2, 3, 4, 5, 6)
    for src, end in blocks:
        arr[src] = end

    del blocks
    print(bfs())


if __name__ == "__main__":
    solution()
