import sys
from typing import List
"""
[풀이]
1) 입력을 통해 하위 문제로 분할
    - Q1: 주어진 숫자 보다 작아지는 수열의 경우를 찾으면서 하나 하나 자리 수를 확정
    - Q2: 첫번째 수열과 입력된 수열의 자리수를 비교
"""


def permutation(n: int) -> int:
    if n in cache:
        return cache[n]

    elif n <= 1:
        return 1

    else:
        cache[n] = n * permutation(n - 1)
        return cache[n]


def solution():
    if S[0] == 1:
        K = S[1]
        src = [i for i in range(1, N+1)]
        result_list = []
        for i in range(N):
            x = permutation(N-1-i)
            step = (K-1) // x
            result_list.append(src[step])
            src.remove(src[step])
            K -= x*step
        print(*result_list)

    else:
        num_list = S[1:]
        src = sorted(num_list)
        result = 1
        for i in range(N):
            step = src.index(num_list[i])
            src.remove(num_list[i])
            x = permutation(N-1-i)
            result += x*step
        print(result)


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    S = list(map(int, sys.stdin.readline().split()))  # material of sub-problem
    cache = {}
    solution()
