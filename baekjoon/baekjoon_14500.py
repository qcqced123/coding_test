import sys
from typing import List


def solution():
    """ 테트로미노: 정사각형 4개 이어붙임
    격자위에 테트로미노 놓고, 합의 최대 구하기, 1,250,000 (완전 탐색 가능)

    idea: Table Search
        1) 5가지 테트로미노 이동 방향 정의
        2) 탐색
            - 탐색하다가 밖으로 나가게 되면 바로 탐색 종료
            - 다음 위치로 이동
            - 회전 대칭이 되는구나 (시계 방향으로 회전시키기자)
    """
    def is_valid() -> bool:
        return -1 < ny < N and -1 < nx < M

    result = 0
    N, M = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    dy = [
        (0, 0, 0, 1, 2, 3),
        (1, 1, 0),
        (1, 2, 2, 0, 0, 1, -1, -2, -2, 0, 0, -1, 1, 2, 2, 0, 0, 1, -1, -2, -2, 0, 0, -1),
        (1, 1, 2, 0, 1, 1, 1, 1, 2, 0, 1, 1),
        (0, 0, 1, 0, 0, -1, 1, -1, 0, 1, -1, 0)
    ]
    dx = [
        (1, 2, 3, 0, 0, 0),
        (0, 1, 1),
        (0, 0, 1, -1, -2, -2, 0, 0, -1, 1, 2, 2, 0, 0, -1, 1, 2, 2, 0, 0, 1, -1, -2, -2),
        (0, 1, 1, -1, -1, -2, 0, -1, -1, 1, 1, 2),
        (-1, 1, 0, -1, 1, 0, 0, 0, -1, 0, 0, 1)
    ]

    for i in range(5):  # 퍼즐 iteration
        cdy, cdx = dy[i], dx[i]  #
        for y in range(N):
            for x in range(M):
                for v in range(0, len(cdy), 3):
                    cnt = grid[y][x]
                    for z in range(3):
                        ny, nx = cdy[v+z] + y, cdx[v+z] + x
                        if is_valid():
                            cnt += grid[ny][nx]
                        else:
                            break
                    else:
                        result = max(result, cnt)
    print(result)


if __name__ == "__main__":
    solution()
