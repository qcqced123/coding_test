import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
arr = [1] * N

for i in range(N):
    tmp = 1
    for j in range(i):
        if num_list[i] < num_list[j] and arr[i] < arr[i] + arr[j]:
            tmp = max(tmp, arr[i] + arr[j])
    arr[i] = tmp
print(max(arr))


