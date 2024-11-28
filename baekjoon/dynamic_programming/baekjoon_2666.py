import sys


def solution():
    """
    idea: dynamic programming
        - 이동 횟수: 현재 사용할 위치(x)와 가장 가까운 빈칸(y)
        - 제약 조건: 어느 빈칸을 선택할까?
            - 행: 순서
            - 열: 빈칸 개수
    feedback:
        - 3차원 dp 캐시 사용
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


def solution2():
    """
    idea: dynamic programming
        - 3D dp cache array
            - 행: 벽장문 길이
            - 열: 벽장문 길이
            - 축: 벽장문 길이
            - 원소: 최소 이용 횟수 (~최소 거리)
    feedback:
        - 이런거 나오면 실전에서 어케 풀지..? 점화식
            - 확실히 이런 문제에 약한거 같아... ㅠ
    """
    # init data structure
    N = int(input())

    M, K = map(int, input().split())
    cache = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]

    L = int(input())
    orders = [int(input()) for _ in range(L)]

    # update the dp cache
    sys.setrecursionlimit(10**6)
    def recursive_func(order, door1, door2):
        if order == L:
            return 0
        x = orders[order]
        cache[x][door1][door2] = min(
            abs(x-door1) + recursive_func(order+1, x, door2),
            abs(x-door2) + recursive_func(order+1, door1, x),
        )
        return cache[x][door1][door2]
    print(recursive_func(0, M, K))


if __name__ == "__main__":
    solution2()
