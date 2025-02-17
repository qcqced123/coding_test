import sys

INF = sys.maxsize
input = sys.stdin.readline


def solution():
    """
    idea: two pointer
        - 포인터 위치:
        - 포인터 이동 방향:
            - left: forward
            - right: backward

        - 포인터 이동 조건:
            - left: 합이 음수일 때
            - right: 합이 양수

    limit: NlogN
    """
    # get input data
    N = int(input())
    arr = list(map(int, input().split()))

    # do two pointer
    answer = INF
    left, right = 0, N-1
    while left < right:
        cnt = arr[left] + arr[right]
        if abs(cnt) < abs(answer):
            answer = cnt

        if cnt >= 0: right -= 1
        else: left += 1

    print(answer)


if __name__ == "__main__":
    solution()
