import sys
from typing import List

"""
[요약]
1) 2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성
    - 길이: 1000
    - 시간: 1초
[전략]
1) 시간이 짭고 메모리 제한이 크기 때문에 Tabulation
"""


def get_tiling(x: int, arr: List[int]) -> int:
    if x > 2:
        for i in range(3, x+1):
            arr[i] = arr[i-1] + 2*arr[i-2]
    return arr[x]


N = int(sys.stdin.readline())
tiling = [0] * (N+1)
tiling[1] = 1

if N > 1:
    tiling[2] = 3

print(get_tiling(N, tiling) % 10007)

