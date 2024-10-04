import sys
from collections import defaultdict


def solution():
    """ 어느 세 점도 일직선 위에 놓이지 않도록, 다시 그을 수는 없지만 이미 그린 다른 선분과 교차 가능
    사이클: 선분을 한 번만 지나서 출발점 돌아가기, 같은 선분 여러번 불가

    idea: disjoint set, union-find
        1)
    """
    def find(x: int) -> int:
        if arr[x] != x:
            find(arr[x])

        return arr[x]

    N, M = map(int, sys.stdin.readline().split())
    arr = list(range(N))


if __name__ == "__main__":
    solution()
