import sys
from collections import deque
"""
[풀이 시간]
1) 22:50 ~ 23:20

[요약]
1) 1: 이동 가능, 0: 이동 불가능
    - 왼쪽 상단 끝에서 오른쪽 하단 끝까지 이동, 이 때 지나야 하는 최소 칸 수
    - 시작 위치, 종료 위치 모두 칸 수에 포함
    - 도착위치로 이동할 수 있는 경우만 입력으로 주어짐
[전략]
1) 테이블 자료구조 & 상하좌우 이동
    - DFS/BFS
    - 둘 중 뭐가 더 편할지는 구현해보면서 생각해보자
    - visited 필요 하려나..?
    - 이걸 BFS로 구현해야겠구나
"""


def bfs(y, x):
    queue = deque([])
    queue.append([y, x])
    while queue:
        vy, vx = queue.popleft()
        for i in range(4):
            ny = vy + dy[i]
            nx = vx + dx[i]
            if 0 <= ny < N and 0 <= nx < M and table[ny][nx] == 1:
                queue.append([ny, nx])
                table[ny][nx] += table[vy][vx]


N, M = map(int, sys.stdin.readline().split())
table = [[int(i) for i in list(sys.stdin.readline().rstrip())] for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

bfs(0, 0)
print(table[-1][-1])



