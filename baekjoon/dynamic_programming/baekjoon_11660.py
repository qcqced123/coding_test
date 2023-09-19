import sys
"""
[요약]
1) n x x 크기 테이블
    - 입력과 실제 인덱스 값 차이 있음
    - 주어진 구간의 모든 원소 합 구하는 프로그램 작성
    - 시간, 메모리, 입력 길이: 1초, 256, 1024
    => Tabulation 가능
[전략]
1) dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i][j]
    - 누적합 배열 만들기
    - 2차원 누적 합은 1차원 누적 합과 완전히 다른 개념!
    - 1행, 1열은 1차원 배열의 누적값으로 먼저 초기화
"""
N, M = map(int, sys.stdin.readline().split())
graph, dp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)], [[0] * (N+1) for _ in range(N+1)]

# 1) init row 0 & col 0
for i in range(N):
    for j in range(N):
        dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1] - dp[i][j] + graph[i][j]  # Cautions! index are different between graph and dp

# 2) calculate target value
for _ in range(M):
    row1, col1, row2, col2 = map(int, sys.stdin.readline().split())
    print(dp[row2][col2] - dp[row1-1][col2] - dp[row2][col1-1] + dp[row1-1][col1-1])
