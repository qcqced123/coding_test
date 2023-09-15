import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
arr = num_list[:]

for i in range(N):
    for j in range(i):
        if num_list[i] > num_list[j] and arr[i] < arr[j] + num_list[i]:
            arr[i] = arr[j] + num_list[i]
print(max(arr))
