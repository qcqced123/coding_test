import sys

"""
1) make dp table (2D)
    - row: text 1
    - col: text 2
=> 바로 위칸을 더하면, 바로 이전 철자까지의 최대값에 +1 하는게 아니라, 현재 철자까지의 최대값에 +1 하게 되는거라 말이 안된다.
"""
text_1 = "%" + sys.stdin.readline().rstrip()
text_2 = "%" + sys.stdin.readline().rstrip()

size_1, size_2 = len(text_1), len(text_2)
dp = [[0]*size_2 for _ in range(size_1)]

for i in range(1, size_1):
    for j in range(1, size_2):
        char_1, char_2 = text_1[i], text_2[j]
        if char_1 == char_2:
            dp[i][j] = dp[i-1][j] + 1

        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])
