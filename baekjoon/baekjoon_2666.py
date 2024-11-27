import sys


def solution():
    """
    idea: dynamic programming
        - 이동 횟수: 현재 사용할 위치(x)와 가장 가까운 빈칸(y)
        - 제약 조건: 어느 빈칸을 선택할까?
            - 행: 순서
            - 열: 빈칸 개수
    feedback:
        - 모르겠음

    """
    # init the data structure
    input = sys.stdin.readline
    N = int(input())
    empty1, empty2 = map(int, input().split())
    K = int(input())
    orders = [int(input()) for _ in range(K)]

    # update the dp cache
    cache = [0]*K
    for i in range(K):
        temp1, temp2 = abs(orders[i] - empty1), abs(orders[i] - empty2)
        if temp1 < temp2:
            empty1 = orders[i]
            cnt = temp1

        else:
            empty2 = orders[i]
            cnt = temp2

        cache[i] = cache[i-1] + cnt
    print(cache[-1])


if __name__ == "__main__":
    solution()
