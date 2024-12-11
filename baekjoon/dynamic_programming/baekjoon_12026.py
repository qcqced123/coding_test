import sys


def solution():
    """
    idea: dynamic programming, N**2
        - B, O, J
        - dp[i]: i번째 블록을 밟는다고 가정, 필요한 에너지의 최소값
    """
    INF = sys.maxsize
    input = sys.stdin.readline
    N = int(input())
    dp = [INF]*N
    vocab = {
        "B": "J",
        "O": "B",
        "J": "O"
    }
    arr = list(input().rstrip())

    # update the dp cache
    dp[0] = 0
    for i in range(1, N):
        cnt = arr[i]
        for j in range(i):
            candidate = arr[j]
            if vocab[cnt] == candidate:
                dp[i] = min(dp[i], dp[j]+(i-j)**2)

    print(dp[-1]) if dp[-1] != INF else print(-1)


if __name__ == "__main__":
    solution()
