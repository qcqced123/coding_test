import sys
from collections import defaultdict, deque

record_list = [False for i in range(9)]
graph = [[],
         [2, 3, 8],
         [1, 7],
         [1, 4, 5],
         [3, 5],
         [3, 4],
         [7],
         [2, 6, 8],
         [1, 7],
         ]
# Step 1. 인접 행렬 => 노드별 간선 연결 집합 출력하기 (+1 해줘야 실제 노드의 번호)
# adj_idx = [[idx for idx, value in enumerate(graph[idx][:]) if value == 1] for idx in range(len(graph))]
# print(adj_idx)
print(graph[1])


# Stack 구조 사용 => 재귀 함수
def dfs(graph, src, visited):
    visited[src] = True
    print(src, end=' ')
    for i in graph[src]:
        if not visited[i]:
            dfs(graph, i, visited)


def iter_dfs(graph, src, visited):
    stack = [src]
    while stack:
        curr = stack.pop()
        if not visited[curr]:
            visited[curr] = 1
            stack.append([nx for nx in graph[curr] if not visited[nx]].reverse())  # reverse(): left-first search
    return


if __name__ == '__main__':
    dfs(graph, 1)