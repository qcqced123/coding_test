from typing import Tuple, List


def my_solution(n):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/68645

    summary:
        1) 맨 위 꼭짓점부터 반시계 방향으로 채우기

    solution:
        1) 하삼각행렬
            1
            2 15
            3 16 14
            4 17 21 13
            5 18 19 20 12
            6 7 8 9 10 11
        2) 이동 배열 미리 정의
        3) 탐색해야 하는 칸의 수를 미리 계산할 수 있으니까, 이걸 조건으로 while-loop 돌리기
    """
    dy, dx = (1, 0, -1, 1), (0, 1, -1, 0)
    table = [[0] * n for _ in range(n)]

    blocks = (n ** 2 - n) // 2 + n - 1
    vy, vx, vd, value = 0, 0, 0, 1

    table[vy][vx] = value
    while blocks:
        ny, nx = vy + dy[vd], vx + dx[vd]
        if -1 < ny < n and -1 < nx < n and not table[ny][nx]:
            value += 1; blocks -= 1
            table[ny][nx] = value
            vy, vx = ny, nx
        else:
            vd = (vd + 1) % 4

    answer = [table[r][c] for r in range(n) for c in range(n) if table[r][c]]
    return answer


def solution(n):
    """ Optimize Ver """
    pass

