import sys

INF = sys.maxsize
input = sys.stdin.readline


def solution():
    """
    idea: two pointer with prefix sum
        - 포인터 위치: 나란히
        - 포인터 방향: forward
        - 포인터 조건: cnt vs sum-cnt
    """
    # get input data
    N = int(input())
    times = [int(input()) for _ in range(N)]

    # init prefix sum array
    prefix = [0]*N
    total = sum(times)
    for i in range(1, N):
        prefix[i] = prefix[i-1] + times[i-1]

    # do two-pointer
    answer = 0
    left, right = 0, 0
    while right < N:
        cnt = prefix[right] - prefix[left]
        answer = max(answer, min(cnt, total-cnt))
        if cnt < total-cnt:
            right += 1
        else:
            left += 1

    print(answer)


if __name__ == "__main__":
    solution()
