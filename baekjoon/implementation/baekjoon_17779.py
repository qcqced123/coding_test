import sys
from typing import List
"""
[요약]
1) 최대한 공평하게 선거구를 획정
    - 재현시: N*N 크기 격자로 표현
    => 개별 격자(구역)을 5개의 영역(선거구)로 나누기
    => 모든 구역은 하나의 선거구에 포함, 모든 선거구는 하나 이상 구역 포함
    => 선거구 내부 구역은 모두 인접 연결, 인접의 의미는 상하 좌우, 대각선
    => 선거구 개수는 무조건 5개로 고정
[풀이]
0) 기준점, 경계 길이 정하기
    - 1 ≤ row ≤ N-d1-d2
    - 1 + d1 ≤ col ≤ N-d2
1) 경계선 긋기
    - 고정된 라인 4개 긋기
2) 선거구 구역 획정•동시에 인구수 계산
    - 1번부터 5번까지 차례대로 선거구 획정
    - 획정하면서 동시에 인구수 계산
=> 모든 인덱스는 입력된 좌표값과 1 차이남
"""


def population(r: int, c: int, d1: int, d2: int, grid: List[List[int]], section: List[int]) -> None:
    """ calculate number of people in each area """
    size, total = len(grid), sum(map(sum, grid))
    # for sector 1
    tmp_col = c
    for x in range(r+d1):
        if x >= r:
            tmp_col -= 1
        section[0] += sum(grid[x][0:tmp_col+1])

    # for sector 2
    tmp_col = c+1
    for x in range(r+d2+1):
        if x > r:
            tmp_col += 1
        section[1] += sum(grid[x][tmp_col:size])

    # for sector 3
    tmp_col = c-d1-1
    for x in range(r+d1, size):
        section[2] += sum(grid[x][0:tmp_col+1])
        if x < r+d1+d2:
            tmp_col += 1

    # for sector 4
    tmp_col = c+d2
    for x in range(r+d2+1, size):
        section[3] += sum(grid[x][tmp_col:size])
        if x <= r+d1+d2:
            tmp_col -= 1

    # for sector 5
    section[4] = total - sum(section)


def area(r: int, c: int, d1: int, d2: int, grid: List[List[int]]) -> int:
    sector = [0] * 5
    population(r, c, d1, d2, grid, sector)
    target = max(sector) - min(sector)
    return target


def solution():
    N = int(sys.stdin.readline())
    people = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # population grid
    result = float('inf')

    for r in range(N-2):
        for c in range(1, N-1):
            for d1 in range(1, c+1):  # 1 + d1 ≤ y
                for d2 in range(1, N-c+1):  # d2 ≤ N - y
                    if r + d1 + d2 < N and c - d1 >= 0 and c + d2 < N:
                        result = min(result, area(r, c, d1, d2, people))
    print(result)


if __name__ == "__main__":
    solution()
