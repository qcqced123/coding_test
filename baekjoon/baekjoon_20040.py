import sys
from collections import defaultdict


def solution():
    """ 어느 세 점도 일직선 위에 놓이지 않도록, 다시 그을 수는 없지만 이미 그린 다른 선분과 교차 가능
    사이클: 선분을 한 번만 지나서 출발점 돌아가기, 같은 선분 여러번 불가

    idea: disjoint, find
    """
    def find(x: int) -> int:
        if arr[x] != x:
            arr[x] = find(arr[x])
        return arr[x]

    def union(y: int, x: int):
        y = find(y)
        x = find(x)

        if y < x:
            arr[x] = y

        else:
            arr[y] = x

    N, M = map(int, sys.stdin.readline().split())
    arr = list(range(N))

    for stage in range(M):
        src, end = map(int, sys.stdin.readline().split())
        if find(src) != find(end):
            union(src, end)

        else:
            print(stage+1)
            break

    else:
        print(0)


if __name__ == "__main__":
    solution()
