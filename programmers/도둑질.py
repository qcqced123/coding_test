def solution(money):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/42897

    summary:
        1) 인접한 두 집을 연속으로 털 수 없다, 특히 원형 큐 형태로 생겼다는 것 주의

        0, 1, 2, 3 (index)
        1, 2, 3, 1 (value)

        0, 1, 2, 3 (index)
        1, 0,

    implementation:
        1) 원형 큐 형태인 것 조심해서 구현


    solution:
        1) DP, 최소 O(NlogN) 이하
          - 주어진 배열 상, 첫 집을 터는지 안터는지에 따라서 경우의 수 분할
          - 그리고 계단밟기 문제처럼 풀면 된다
          - 점화식: max(dp[i-2], dp[i-3]) + table[i]
    """
    size = len(money)
    dp = [[0] * size for _ in range(2)]  # 1행 => 첫번째 집 방문, 2행 => 방문 x
    dp[0][0], dp[1][1] = money[0], money[1]
    for i in range(2, size):
        if i == 2:
            dp[0][i] = dp[0][i-2] + money[i]
            dp[1][i] = max(dp[1][i - 1], money[i])
            continue

        if i == size - 1:
            dp[1][i] = max(dp[1][i - 3], dp[1][i - 2]) + money[i]

        else:
            dp[0][i] = max(dp[0][i-3], dp[0][i-2]) + money[i]
            dp[1][i] = max(dp[1][i-3], dp[1][i-2]) + money[i]

    return max(max(dp[0]), max(dp[1]))


if __name__ == '__main__':
    solution([1, 1, 4, 1, 4])
