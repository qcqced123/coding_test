import sys


def solution():
    """ 부분합 문제 (두 수의 합)
    idea: two-pointer
        1) sort array
        2) init two-pointer
            - position of pointer: 양 끝
            - direction of pointer: forward, backward
            - condition of moving pointer:
            - condition of breaking loop: l < r

    1, 2, 3, 4, 5, 7
    """
    N = int(input())
    M = int(input())  # target value
    nums = list(map(int, sys.stdin.readline().split()))

    nums.sort()
    result = 0
    left, right = 0, N-1
    while left < right:
        cnt = nums[left] + nums[right]
        if cnt == M:
            result += 1
            left += 1

        elif cnt > M:
            right -= 1

        elif cnt < M:
            left += 1

    print(result)


if __name__ == "__main__":
    solution()
