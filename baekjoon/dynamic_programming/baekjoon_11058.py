import sys
from typing import List
"""
[풀이]
1) 2번을 누를 때, 이미 버퍼는 empty가 아님
    - max((dp[N-4]*3, dp[N-5]*4, ... ))
"""


def solution():
    N = int(sys.stdin.readline())
    dp = [0] * (N+1)
    for i in range(1, N+1):
        if i < 7:
            dp[i] = i
            continue
        tmp = [dp[i-k]*(k-1) for k in range(4, i)]
        dp[i] = max(tmp)
    print(dp[N])


if __name__ == "__main__":
    solution()
