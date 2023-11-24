import sys
from collections import deque
from typing import List, Tuple
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


def dfs(y: int, x: int, bag: List[Tuple]):
    ny = y + 1
    if ny < N and graph[ny][x] > -1:
        bag.append((ny, x))
        dfs(ny, x, bag)
    elif ny < N and graph[ny][x] == -1:




def bfs(y: int, x: int, v: int, visit: List[List]):
    visit[y][x] = True
    q, tmp, rainbow = deque([(y, x)]), [(y, x)], 0
    while q:
        vy, vx = q.popleft()
        for i in range(4):
            ny = dy[i] + vy
            nx = dx[i] + vx
            if -1 < ny < N and -1 < nx < N and (graph[ny][nx] == v or not graph[ny][nx]) and not visit[ny][nx]:
                if not graph[ny][nx]:
                    rainbow += 1
                visit[ny][nx] = True
                tmp.append((ny, nx))
                q.append((ny, nx))
    tmp.sort()
    return tmp, rainbow


def solution():
    # 1) 영역이 가장 넓은 블럭 그룹 찾기
    result = 0
    blocks, curr, curr_rainbow = [], 2, 0
    for color in range(1, M+1):
        for r in range(N):
            for c in range(N):
                visited = [[False] * N for _ in range(N)]
                if graph[r][c] == color and not visited[r][c]:
                    block, count = bfs(r, c, color, visited)
                    if len(block) > curr:
                        blocks = block
                        curr = len(block)
                        curr_rainbow = count
                    elif len(block) == curr:
                        if count > curr_rainbow:
                            blocks = block
                            curr_rainbow = count
                        elif count == curr_rainbow:
                            if block[0][0] > blocks[0][0]:
                                blocks = block
                                curr_rainbow = count
                            elif block[0][0] == blocks[0][0]:
                                if block[0][1] > blocks[0][1]:
                                    blocks = block
                                    curr_rainbow = count
    # 2) 블럭 폭파, 점수 계산
    result += len(blocks)**2
    for block in blocks:
        i, j = block
        graph[i][j] = -2
    # 3) 중력 적용
    for c in range(N):
        for r in range(N):
            if graph[r][c] > -1:
                tmp_bag = [(r, c)]
                dfs(r, c, tmp_bag)


if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    N, M = map(int, sys.stdin.readline().split())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    solution()
