import sys
"""
[요약]
1) 빨파초 규칙에 맞게 칠하되, 최소의 비용을 사용
    - 입력: 1000
    - 시간: 0.5초
    => Tabulation
    - 양쪽 집이랑 색이 달라야 함
    - 이웃 집이랑 겹치지 않는 가운데, 전체 비용이 최소가 되도록
    - 어느 조합이 마지막에 제일 최소가 될지 알 수 없기 때문에 모두 traced 해줄 필요가 있음
"""
n = int(sys.stdin.readline())
dp = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = [[0]*3 for _ in range(n+1)]

for i in range(1, n+1):
    ans[i][0] = min(ans[i-1][1], ans[i-1][2]) + dp[i-1][0]  # Red case traced
    ans[i][1] = min(ans[i-1][0], ans[i-1][2]) + dp[i-1][1]  # Green case traced
    ans[i][2] = min(ans[i-1][0], ans[i-1][1]) + dp[i-1][2]  # Blue case traced
print(min(ans[n][0], ans[n][1], ans[n][2]))
