def solution(triangle):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/43105

    solution:
        1) 정사각형 테이블로 변경
        2) 바로 아래, 오른쪽 대각선만 이동 가능
    """
    table, dp = [[0] * len(triangle) for _ in range(len(triangle))], [[0] * len(triangle) for _ in range(len(triangle))]
    for r in range(len(triangle)):
        for c in range(len(triangle[r])):
            table[r][c] = triangle[r][c]

    dp[0][0] = table[0][0]  # init dp
    for r in range(len(table) - 1):
        for c in range(r + 1):
            dp[r + 1][c] = max(dp[r + 1][c], table[r + 1][c] + dp[r][c])
            dp[r + 1][c + 1] = max(dp[r + 1][c + 1], table[r + 1][c + 1] + dp[r][c])

    return max(dp[-1])


if __name__ == '__main__':
    solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
