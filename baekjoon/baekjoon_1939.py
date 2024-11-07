import sys
from collections import defaultdict


def solution():
    """ NlogN, 중량의 최대값, 이동: 공장1 to 공장2 (방향 제한은 없고)
    결국 이동 경로상에 존재하는 다리들의 조합 중에서, 중량 제한의 최소값이 중요함

    idea: binary search with hash
        - 가능한 경로 경우의 수부터 만들어야 할 것 같은데...?
        - 탐색 대상/범위: 중량 배열
        - 탐색 기준: 현재 "중량값"이 최대값이 되려면..? 만약 경로 중에 현재 기준값보다 큰게 나오면..?
            -
    implement:
        - 경로 탐색을 어떻게 효율적으로 할거야..?
        - 경로를 탐색하면서, 중량 제한이 가장 크게 유지되도록 만들어야 되는데,,

    question:
        - 경로를 효율적으로 만들어 줘야 하는데, 그걸 못하겠음
        - 그렇다고 무작정 단일 다리의 중량 제한으로 탐색 기준을 세팅할 수도 없음
    """
    input = sys.stdin.readline
    N, M = map(int, input().split())  # 섬, 다리

    # init pointer and make graph
    l, r = 0, 0
    graph = defaultdict(list)
    for _ in range(M):
        src, end, limit = map(int, input().split())
        graph[src].append((limit, end))
        r = max(r, limit)

    src_point = list(map(int, input().split()))
    while l <= r:
        mid = (l+r) // 2
        for src in src_point:
            for nw, nx in graph[src]:
                pass


if __name__ == "__main__":
    solution()
