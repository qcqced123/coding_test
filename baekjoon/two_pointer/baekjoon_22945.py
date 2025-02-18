import sys

INF = sys.maxsize
input = sys.stdin.readline


def solution():
    """
    idea: two pointer
        - 포인터 위치: 양 끝
        - 포인터 이동 방향:
            - left: forward
            - right: backward

        - 포인터 이동 조건: 양끝에 두고 계속 줄여 나가면, 길이 값이 계속 감소하기 때문에, 이것을 보존하려면 현재 더 작은 값을 가리키는 것을 옮기자
    """
    # get input data
    N = int(input())
    arr = list(map(int, input().split()))

    # do two pointer
    answer = 0
    left, right = 0, N-1
    while left < right:
        cnt_l, cnt_r = arr[left], arr[right]
        answer = max(answer, min(cnt_l, cnt_r)*(right-left-1))
        if cnt_l < cnt_r:
            left += 1

        else:
            right -= 1

    print(answer)


if __name__ == "__main__":
    solution()
