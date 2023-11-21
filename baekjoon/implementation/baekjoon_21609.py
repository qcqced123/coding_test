import sys
from collections import deque
from typing import List
"""
[요약]
- 블럭 종류: 3개
- 인접: 상하좌우
- 블럭 그룹: 일반 1개 이상, 색 모두 같아야, 검정 X, 무지개 치트키, 그룹 내 모든 블럭은 서로 인접
- 기준 블럭: 1순위 행번호 가장 작은거, 2순위 열번호 가장 작은거
[풀이]
1) 영역이 가장 넓은 블럭 그룹 찾기
    - 그룹 찾는다고 탐색하면서 동시에 아래 필요한 모든 정보를 저장하면서 가야할 듯
    - 동순위: 무지개 블럭 수 많은거, 기준 블록의 행이 가장 큰 것, 기준 블록의 열이 가장 큰 것
    - 모든 블럭 소각, 블럭 개수만큼 점수 획득
2) 중력 적용
    - 검은색 블록을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동
3) 반시계 방향 90도 회전
4) 중력 적용
"""


def bfs(y: int, x: int, value: int) -> List:
    tmp = []
    q = deque([])
    q.append((y, x)), tmp.append((y, x))
    while q:
        vy, vx = q.popleft()
        for i in range(4):
            ny = dy[i] + vy
            nx = dx[i] + vx
            if -1 < ny < N and -1 < nx < N and (graph[ny][nx] == value or graph[ny][nx] == 0) and not visited[ny][nx]:
                if graph[ny][nx] == value:
                    visited[ny][nx] = True
                tmp.append((ny, nx))
                q.append((ny, nx))
    return tmp


def solution():
    # 1) 가장 넓은 영역의 블럭 그룹 찾기: 일반 블럭이 하나 이상 포함, 일반 블럭 기준으로 찾기

    for n in range(1, M+1):
        for i in range(N):
            for j in range(N):
                if graph[i][j] == n:
                    block = bfs(i, j, n)
                    if len(block) > 1:
                        blocks.append(block)
    print(blocks)


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    blocks = []
    solution()
