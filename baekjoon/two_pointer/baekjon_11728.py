import sys
from typing import List


def solution():
    """ 주어진 두 배열을 합치고, 오름차순 정렬한 배열 출력, NlogN 이내
    병합 정렬: NlogN (conquer: logN, merge: N)
    idea:
        1) 병합 정렬의 conquer 부분 구현

    solution:
    """
    def combine():
        result = []
        left, right = 0, 0
        while left < N and right < M:
            if arr1[left] < arr2[right]:
                result.append(arr1[left])
                left += 1

            else:
                result.append(arr2[right])
                right += 1

        # 어차피 둘 중 한 쪽에만 원소가 남아 있어서 코드 적는 순서는 상관 X, 근데 어디가 남을지 컴퓨터 입장에서는 모르니까
        result += arr1[left:]
        result += arr2[right:]
        return result

    N, M = map(int, sys.stdin.readline().split())
    arr1 = list(map(int, sys.stdin.readline().split()))  # cast element to int
    arr2 = list(map(int, sys.stdin.readline().split()))

    for i in combine():
        print(i, end=' ')


if __name__ == "__main__":
    solution()
