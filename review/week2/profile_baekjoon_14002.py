import sys
try:
    profile
except NameError:
    profile = lambda x: x

@profile
def main():
    N = int(sys.stdin.readline())
    num_list = list(map(int, sys.stdin.readline().split()))
    arr, num_arr = [1] * N, [[num_list[i]] for i in range(N)]
    for i in range(1, N):
        for j in range(i):
            if num_list[i] > num_list[j] and arr[i] < arr[j] + 1:  # 비교를 tmp랑 해야 정확하다.
                arr[i] = arr[j] + 1
                num_arr[i] = num_arr[j] + [num_list[i]]

    result = max(arr)
    num_idx = arr.index(result)
    print(result)
    print(*num_arr[num_idx])  # python asterisk: unpacking iterable object


if __name__ == '__main__':
    main()
