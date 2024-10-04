import sys
from collections import deque
from collections import defaultdict


def solution():
    """ 키 일대일 비교, 일부 비교 결과만 주어짐, 3,200,000,000 (N*M 이하)
    학생들 순서 매기기, 위상 정렬

    idea: topological sort
        1) 그래프 초기화
        2) 캐시 초기화
    """
    N, M = map(int, sys.stdin.readline().split())  # 학생 숫자, 간선 개수

    # initialize the graph, caches
    cache = [0] * (N+1)
    graph = defaultdict(list)
    for _ in range(M):
        src, end = map(int, sys.stdin.readline().split())
        graph[src].append(end)
        cache[end] += 1

    # initialize the queue for bfs
    q = deque([])
    for i in range(1, N+1):
        if not cache[i]:
            q.append(i)

    # do bfs
    result = []
    while q:
        vx = q.popleft()
        result.append(vx)
        for nx in graph[vx]:
            cache[nx] -= 1
            if not cache[nx]:
                q.append(nx)

    print(*result) if len(result) == N else print(0)


if __name__ == "__main__":
    solution()
