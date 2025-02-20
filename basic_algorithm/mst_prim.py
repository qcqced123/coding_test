import sys, heapq
from typing import List


def prim(grid: List[List], visit: List[bool], start: int) -> int:
    """ prim is the node-based algorithm for making the mst(minimum spanning tree)
    """
    visit[start] = True
    tmp = grid[start]  # 선택된 노드에 대한 모든 인접 간선 추출
    heapq.heapify(tmp)  # 이미 생성되어 있는 자료구조에 대해서는 heapq.heapify를 사용하면 힙 성질을 만족하도록 할 수 있다
    mst, total = [], 0
    while tmp:
        weight, u, v = heapq.heappop(tmp)
        if not visit[v]:  # 미방문 노드로의 간선만 선택하는 방식으로, 사이클 발생 여부 판정하는 알고리즘을 구현
            visit[v] = True
            mst.append((u, v))
            total += weight
            for edge in graph[v]:
                if not visit[edge[2]]:
                    heapq.heappush(tmp, edge)
    return total


def solution():
    result = prim(graph, visited, 1)  # 시작 노드를 어떤 것으로 설정해도 상관 없음
    print(result)


if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    graph, visited = [[] for _ in range(V+1)], [False]*(V+1)
    for _ in range(E):
        src, end, cost = map(int, sys.stdin.readline().split())
        graph[src].append([cost, src, end])
        graph[end].append([cost, end, src])
    solution()
