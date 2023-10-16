import sys
from typing import List


def solution():
    T = int(sys.stdin.readline())
    t_case = [int(sys.stdin.readline()) for _ in range(T)]

    # 1) 테스트 케이스 내부에서 가장 큰 수 기준, 소수 배열 한 번만 게산
    t_max = max(t_case)
    arr = [0] * (t_max+1)
    arr[0], arr[1] = 1, 1
    for i, num in enumerate(arr):
        if num:  # 소수 아닌 경우 처리
            continue
        for j in range(i + i, len(arr), i):
            arr[j] = 1

    for t in t_case:
        result = 0
        for k in range(2, int(t/2) + 1):
            if not arr[k] and not arr[t-k]:
                result += 1
        print(result)


if __name__ == "__main__":
    solution()