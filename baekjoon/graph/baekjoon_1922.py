import sys
from typing import List
"""
[조건]
1) 모든 컴퓨터가 연결 상태
    - 연결 상태 == 간선 혹은 경로 존재
    - 모든 컴퓨터를 최소 비용으로 연결
[풀이]
1) 개별 노드를 시작 노드로 iteration
    - 모든 노드에 도달 가능한 경로가 존재하는가
    - 가능한 경로 중에서 최소 비용 경로 찾기
    => 얘는 최소 스패닝 트리를 찾아보고 풀자 의미없다 이렇게 푸는게
"""


def solution():
    # 1) 노드 별로 iteration
    for i in range(1, N+1):
        visited = [False] * (N+1)
        visited[0], visited[i] = True, True
        for n, c in graph[i]:
            pass



if __name__ == "__main__":
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    graph, cost = [[] for _ in range(N+1)], [0] + [float('inf')]*N  # connection information, cost array
    for _ in range(M):
        src, end, cost = map(int, sys.stdin.readline().split())
        graph[src].append([end, cost])
    solution()
