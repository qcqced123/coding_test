import sys


def solution():
    """
    idea: dynamic programming
        - dp[i][j] = i번쨰 동전까지 고려했을 떄, j 값 표현 가능한 모든 경우의 수
        - 동전 개수도 루프로 추가해서, 트리플 루프로 해결 가능함
            - 난 트리플 루프까지 하면 10억이라 당연히 터질줄 알았지
    """
    # make dp cache
    input = sys.stdin.readline
    N = int(input())
    size = int(input())
    dp = [[0]*(N+1) for _ in range(size+1)]
    arr = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(size)]

    # update dp cache
    dp[0][0] = 1
    for i in range(1, size+1):
        coin, left = arr[i]
        for j in range(N+1):
            dp[i][j] = dp[i-1][j]
            for k in range(1, left+1):
                z = j - coin*k
                if z >= 0:
                    dp[i][j] += dp[i-1][z]
    print(dp[-1][-1])


if __name__ == "__main__":
    solution()
