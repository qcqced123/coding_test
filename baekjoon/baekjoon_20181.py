import sys


def solution():
    """ 이동 방향: left to right, 초당 1칸씩 오른쪽으로, 1칸 가는데 1초 소모, NlogN
    idea: prefix sum + dynamic programming + sliding window (two-pointer)
        - dp[i] = max(dp[i-1], dp[lower] + prefix[i] - prefix[lower-1] - K)

    question:
        - 하... 아무리 봐도 맞는데?? 왜 틀리지.......
    """
    # get input data
    input = sys.stdin.readline
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    # find the minimum index of bug by using two-pointer
    cnt = 0
    checker = 0
    bugs = [0]*N
    for i in range(N):
        curr = arr[i]
        bugs[i] = checker
        if cnt + curr < K:
            cnt += curr

        else:
            cnt = curr
            checker = i

    # init the prefix array
    prefix = [0]*N
    prefix[0] = arr[0]
    for i in range(1, N):
        prefix[i] = prefix[i-1] + arr[i]

    # do dynamic programming
    dp = [0]*N
    dp[0] = max(0, arr[0]-K)
    for i in range(1, N):
        lower = bugs[i]
        if lower > 0:
            lower -= 1
        dp[i] = max(dp[i-1], dp[lower] + prefix[i] - prefix[lower] - K)

    print(arr)
    print(prefix)
    print(bugs)
    print(dp)

    print(max(dp))


if __name__ == "__main__":
    solution()
