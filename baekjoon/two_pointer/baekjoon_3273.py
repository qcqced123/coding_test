import sys


def solution():
    """ 두 수의 합, 연속된 숫자 아님
    idea: two-pointer
        1) 배열 정렬
        2) 포인터 설정 초기화
            - 포인터 위치: 양쪽 끝
            - 포인터 이동 방향: forward, backward
            - 포인터 이동 조건:
                - == target value: 왼쪽 포인터 이동
                - > target value: 오른쪽 포인터 이동
                - < target value: 왼쪽 포인터 이동
            - 탐색 종료 조건:
                - left < right
    """
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split()))
    x = int(input())

    nums.sort()
    l, r, result = 0, len(nums) - 1, 0
    while l < r:
        cnt = nums[l] + nums[r]
        if cnt == x:
            result += 1
            l += 1

        elif cnt > x:
            r -= 1

        else:
            l += 1

    print(result)


if __name__ == "__main__":
    solution()
