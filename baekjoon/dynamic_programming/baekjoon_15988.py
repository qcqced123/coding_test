import sys


def solution():
    """ 정수 N을 1,2,3의 조합으로 표현하는 방법, O(N)
    idea: dynamic programming
        - 점화식: dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    implement:
        - 미리 입력 최대치까지 전부 dp 캐시 채우고, 들어오는 입력마다, 인덱싱해서 값을 리턴하도록 만들어야
        - 이래야 시간초과가 나지 않는다
        - 들어오는 입력까지만 dp 캐시 채우는 방식으로 짜면, 입력이 개많아지면 리스트 생성을 개많이 해야 해서 엄청 오래걸리고, 시간 초과가 남
    """
    input = sys.stdin.readline
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    dp = [0] * 1000001
    dp[1], dp[2], dp[3] = 1, 2, 4
    for i in range(4, 1000001):
        dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009

    for n in arr:
        print(dp[n])


if __name__ == "__main__":
    solution()
