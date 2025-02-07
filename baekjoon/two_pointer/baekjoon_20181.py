import sys


def solution():
    """ 1칸 가는데 1초 소모, NlogN
    idea: prefix sum + dynamic programming + sliding window (two-pointer)
        - find te minimum index of current array element
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
        dp[i] = max(dp[i-1], dp[lower] + max(0, prefix[i] - prefix[lower] - K))

    print(max(dp))


def solution2() -> None:
    """
    idea: dynamic programming with two-pointer
        - 포인터 위치: 나란히
        - 포인터 이동 방향: forward
        - 포인터 이동 조건:
            - l forward:
            - r forward:
        - dp[i]: i-th 원소까지 고려했을 때, 최대 탈피 에너지

    feedback:
        - 내가 푼 방식은 중복 되는 원소가 발생 해서 틀림, 구간끼리 겹치면 안되는데, 겹치게 계산이 되어서 그런듯

    """
    # get input data
    input = sys.stdin.readline
    N, K = map(int, input().split())
    arr = [0] + list(map(int, input().split()))

    # two-pointer with dynamic programming
    dp = [0]*(N+1)
    left, right, cnt = 0, 1, 0
    while right <= N:
        cnt += arr[right]  # current total value
        dp[right] = dp[right-1]
        while cnt >= K:
            dp[right] = max(dp[right], dp[left-1] + cnt - K)
            cnt -= arr[left]
            left += 1

        right += 1

    print(dp[N])


if __name__ == "__main__":
    solution2()
