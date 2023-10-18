import sys
from typing import List
from collections import deque
"""
[조건]
1) 같은 색상 사이클 그래프 존재 여부 판단
    - 최소 점 4개 이상
[풀이]
1) 입력 - 순회 시작 - 조건 판별 - 순회 종료
    - 순회 종료: 최초의 사이클 찾으면 바로 종료
    - 사이클 판정 방법: 지하철 순환선 찾기 문제랑 비슷함
        - 주위에 같은게 2개 이상 있는지 판정
        - 있으면 탐색 시작, count == 1일 때는 src 기록
        - count ≥ 4 and 다음 탐색 위치가 src라면 사이클 판정
"""


def dfs(y: int, x: int, count: int, y_src: int, x_src: int, visit: List[List[bool]]) -> None:
    # 1) 주위에 같은게 2개 이상 인지 판정
    visit[y][x] = True
    cnt, stack = 0, []
    for i in range(4):
        ty = dy[i] + y
        tx = dx[i] + x
        if -1 < ty < N and -1 < tx < M and grid[ty][tx] == grid[y][x]:
            cnt += 1
            stack.append([ty, tx])
    if cnt < 2:
        return

    # 2) 탐색 시작
    for ny, nx in stack:
        if not visit[ny][nx]:
            dfs(ny, nx, count+1, y_src, x_src, visit)
            visit[y][x] = True
        # 3) 사이클 판정
        if count >= 4 and visit[ny][nx] and ny == y_src and nx == x_src:
            print("Yes")
            exit()


def solution():
    for i in range(N):
        for j in range(M):
            visited = [[False]*M for _ in range(N)]
            dfs(i, j, 1, i, j, visited)

    print("No")


if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    N, M = map(int, sys.stdin.readline().split())
    grid = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(N)]
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    solution()
