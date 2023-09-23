import sys
from typing import List
from collections import deque

"""
[요약]
1) 시간, 메모리, 입력: 2초, 넉넉, 10만..
2) 걷거나 순간이동
    - 걷기: 1초 소모, 한 칸 이동
    - 순간이동: 1초 소모, 앞으로 2배
    - 동생을 찾을 수 있는 가장 빠른 시간
[풀이]
1) DFS & BackTracking 느낌
    => 재귀 호출 제한 때문에 안된다
2) BFS

"""


def bfs(x: int, y: int) -> int:
    graph[x] = 0
    q = deque([])
    q.append(x)
    while q:
        vx = q.popleft()
        for i in move:
            nx = vx * 2 if i == 2 else vx + i
            if -1 < nx < 100001 and graph[nx] == -1:
                graph[nx] = graph[vx] + 1
                q.append(nx)

            if nx == y:  # 제일 먼저 도착 하는게 가장 빠른 방법이라서
                return graph[nx]


N, K = map(int, sys.stdin.readline().split())
graph = [-1] * 100001  # 수빈이가 동생의 좌표를 넘어갈수도 있기 때문에 최대한 크게 설정해주는게 좋음
move = [-1, 1, 2]
print(bfs(N, K))