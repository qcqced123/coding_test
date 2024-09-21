import sys


def solution():
    """ A -> B, 자신보다 작은 물고기만 먹을 수 있음, 머지 소트랑 비슷할거 같은데
    idea 1: N**2
        테스트 케이스도 여러 개라서 시간초과 날듯

    idea 2: linear search + bisect, NlogN
        1) 일단 정렬
        2) A의 원소가 B의 어느 인덱스(왼쪽)에 위치하는지 찾기
    """
    def bisect_left(arr, v) -> int:
        l, r = 0, len(arr)
        while l < r:
            mid = (l+r) // 2
            if v > arr[mid]:
                l = mid + 1

            else:
                r = mid

        return l

    for _ in range(int(input())):
        N, M = map(int, sys.stdin.readline().split())  # number of A, B
        A = list(map(int, sys.stdin.readline().split()))  # array of A
        B = list(map(int, sys.stdin.readline().split()))  # array of B

        total = 0
        A.sort(), B.sort()
        for e in A:
            total += bisect_left(B, e)

        print(total)


if __name__ == "__main__":
    solution()
