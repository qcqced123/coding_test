import sys
"""
[요약]
1) 가장 긴 부분 수열의 길이, 수열 자체 출력
"""

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
arr, num_arr = [1] * N, [[] for _ in range(N)]
for i in range(N):
    tmp = 1
    for j in range(i):
        if num_list[i] > num_list[j] and arr[i] < arr[j] + arr[i]:
            tmp = max(tmp, arr[j] + arr[i])
    arr[i] = tmp
print(max(arr))
