import sys

INF = sys.maxsize
input = sys.stdin.readline


def solution():
    """
    idea: two pointer
        - 포인터 위치: 나란히
        - 포인터 방향: forward
        - 포인터 이동 조건:
            - left: > M
            - right: < M
    """
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # do two pointer
    cnt = 0
    answer = 0
    left, right = 0, 0
    while right < N:
        cnt += arr[right]
        if cnt > M:
            while cnt > M:
                cnt -= arr[left]
                left += 1

        right += 1
        answer = max(answer, cnt)

    print(answer)


if __name__ == "__main__":
    solution()
