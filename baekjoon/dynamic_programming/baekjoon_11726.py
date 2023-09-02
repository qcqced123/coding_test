import sys
from typing import List
"""
[시간]
1) 02:50 ~ 03:20
[요약]
1) 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램 작성
    - 세로 길이는 고정, 가로 크기가 가변
[전략]
1) f(N) = f(N-1) + f(N-2)
    - 입력 길이: 1000
    - 시간 제한: 1초
    => 제발 하나 하나 차근 차근 더하자...
    => Memoization으로 풀면 개느림
"""


def tiling(x: int, arr: List) -> int:
    if x > 2:
        for i in range(3, x+1):
            arr[i] = arr[i-1] + arr[i-2]
    return arr[x]


N = int(sys.stdin.readline())
array = [0] * (N+1)
array[1] = 1
if N != 1:
    array[2] = 2

print(tiling(N, array) % 10007)
