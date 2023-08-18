from collections import deque

visited = [False for i in range(9)]
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


def bfs(graph, src, visited):
    queue = deque([src])
    visited[src] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


if __name__ == '__main__':
    bfs(graph, 1, visited)
