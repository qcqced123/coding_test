import sys
from typing import List

"""
[요약]
1) 바이토닉 수열: 왼쪽은 증가, 오른쪽은 감소
    - 단조 증가, 감소도 바이토닉으로 처리
    - 시간, 메모리, 입력: 1초, 넉넉, 1000
        => O(N^2)보다 빠른 알고리즘 설계 필요
    - 가장 긴 부분 바이토닉 수열 찾기
"""
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
dp_left, dp_right = [1] * N, [0] * N
# 1) init dp left
for i in range(N):
    for j in range(i):
        if nums[i] > nums[j] and dp_left[i] < dp_left[j] + 1:
            dp_left[i] = dp_left[j] + 1

# 2) init dp right
for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if nums[i] > nums[j] and dp_right[i] < dp_right[j] + 1:
            dp_right[i] = dp_right[j] + 1
dp = [i+j for i, j in zip(dp_left, dp_right)]
print(max(dp))
