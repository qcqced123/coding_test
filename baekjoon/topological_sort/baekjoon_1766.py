import sys
import heapq
from collections import defaultdict


def solution():
    """ 난이도 순서, 번호 클수록 어려움, 세트 문제
    condition:
        1) N개 다 풀어야 함
        2) 세트 문제 순서 지켜서 풀기
        3) 쉬운 문제부터 풀기

    idea: topological sort with priority queue
        1) 작은 번호 푸는게 좋다는 조건이 거슬림
            - 큐를 일반 큐 대신에 우선순위 큐를 사용하자
    """
    input = sys.stdin.readline
    N, M = map(int, input().split())

    # initialize the cache, graph
    cache = [0]*(N+1)
    graph = defaultdict(list)
    for _ in range(M):
        src, end = map(int, input().split())
        cache[end] += 1
        graph[src].append(end)

    # get starting point of searching
    # with priority queue
    h = []
    for i in range(1, N+1):
        if not cache[i]:
            heapq.heappush(h, i)

    result = []
    while h:
        vx = heapq.heappop(h)
        result.append(vx)
        for nx in graph[vx]:
            cache[nx] -= 1
            if not cache[nx]:
                heapq.heappush(h, nx)

    print(*result)


if __name__ == "__main__":
    solution()
