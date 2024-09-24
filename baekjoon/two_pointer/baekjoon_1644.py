import sys
from typing import List


def solution():
    """ 연속된 소수의 합, "연속" 수열 문제를 소수로 변형, 연속된 소수 수열의 합으로 표현 가능한가 출력, NlogN 미만
    idea: two-pointer
        1) 소수 배열 초기화: 에라토스테네스의 체
        2) 포인터 초기화 (모든 경우의 수 세기)
            - 포인터 위치: 나란히 (연속, 겹치는 것 가능)
            - 포인터 방향: forward
            - 포인터 이동 조건:
                - < N: right forward
                - >= N: left forward
    """
    def get_prime():
        prime = []
        arr = [1]*(N+1)
        arr[0], arr[1] = 0, 0
        for i in range(2, N+1):
            if arr[i]:
                prime.append(i)
                for j in range(2 * i, N+1, i):
                    arr[j] = 0

        return prime

    N = int(input())
    nums = get_prime()
    if N == 1:
        print(0)
        exit()

    l, r, result = 0, 0, 0
    l_cache, r_cache = 0, 0

    cache = nums[l]
    while r < len(nums):
        if l_cache != l:
            cache -= nums[l_cache]
            l_cache = l

        elif r_cache != r:
            cache += nums[r]
            r_cache = r

        if cache < N:
            r += 1

        else:
            if cache == N:
                result += 1
            l += 1

    print(result)


if __name__ == "__main__":
    solution()
