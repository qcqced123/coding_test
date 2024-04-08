def solution(n):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/12900

    solution:
        1) Dynamic Programming
          - 점화식: f(n) = f(n-1) + f(n-2) (n >= 3)
          - 처음 어떤 타일을 선택하는가에 따라서 두가지 경우의 수로 나뉜다
    """
    dp = [0]*(n+1)
    for i in range(1, n+1):
        if i <= 2:
            dp[i] = i
            continue
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007  # 이렇게 해야 시간 초과 안난다
    return dp[n]


if __name__ == '__main__':
    solution(10)
