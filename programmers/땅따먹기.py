from typing import Tuple, List


def solution(land):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/12913

    summary:
        1) 같은 열을 연속으로 밟을 수 없다
          - 그럼 나머지 3개의 열은 아무거나 밟아도 된다는 말씀
        => 최대값 리턴
    solution:
        1) DP
          - i번째 행에서 j번째 열을 밟는다고 가정하고, 점화식 세우기
          dp[i][0] = max(dp[i-1][1], dp[i-1][2], dp[i-1][3]) + land[i][0]
          dp[i][1] = ...
          ...
    """
    size = len(land)
    dp = [[0] * 4 for _ in range(size + 1)]
    for i in range(1, size + 1):
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][2], dp[i - 1][3]) + land[i - 1][0]
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][2], dp[i - 1][3]) + land[i - 1][1]
        dp[i][2] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][3]) + land[i - 1][2]
        dp[i][3] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2]) + land[i - 1][3]

    return max(dp[-1])


if __name__ == '__main__':
    solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])