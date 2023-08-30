import sys
from collections import deque
from typing import List

"""
[시간]
1) 16:50 ~ 17:20
[요약]
1) 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력
    - 영역 구분 및 넓이가 가장 큰 영역의 넓이 구하는 프로그램 작성
    - 상하좌우 1로 연결된 것이 그림
[전략]
1) BFS
    - 시간은 넉넉함
    - 조건문에서 다중조건 쓸 때 순서 유의해서 작성하기
"""


def bfs(y: int, x: int, visit: List[bool]) -> int:
    visit[y][x] = True
    queue = deque()
    queue.append([y, x])
    count = 1
    while queue:
        vy, vx = queue.popleft()
        for i in range(4):
            ny = dy[i] + vy
            nx = dx[i] + vx
            if -1 < ny < N and -1 < nx < M and paper[ny][nx] == 1 and not visit[ny][nx]:
                visit[ny][nx] = True
                queue.append([ny, nx])
                count += 1
    return count


N, M = map(int, sys.stdin.readline().split())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

result = []
for i in range(N):
    for j in range(M):
        if paper[i][j] == 1 and not visited[i][j]:
            result.append(bfs(i, j, visited))

print(len(result))
print(max(result) if len(result) != 0 else 0)
