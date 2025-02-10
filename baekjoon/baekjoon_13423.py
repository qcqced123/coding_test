import sys
from bisect import bisect_left


def solution():
    """
    idea: two pointer with bisect
        - sort
        - init two pointer
        - find the element with bisect
    limit: N^2 * logN
    """
    # get input
    input = sys.stdin.readline

    # test case loop
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        arr.sort()

        # init two pointer, find the elemnt with bisect
        answer = 0
        l, r = 0, 1
        while l < N-2:
            for i in range(N-r-1):
                r += i
                if r < N:
                    distance = arr[r] - arr[l]
                    cnt = distance + arr[r]
                    idx = bisect_left(arr, cnt)
                    if r < idx < N and arr[idx] == cnt:
                        answer += 1

            l += 1
            r = l + 1

        print(answer)

if __name__ == "__main__":
    solution()
