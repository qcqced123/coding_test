import sys
"""
[풀이 시간]
1) 00:35 ~ 01:00

[요약]
1) 주어진 트리에서 지정 노드를 삭제 했을 때 남는 리프 노드 개수 출력

[전략]
1) DFS 구현해서 지정 노드가 루트 노드인 하위 트리를 탐색
"""
append_num = 0


def dfs(src):
    global append_num
    for t_node in graph[src]:
        if not visited[t_node] and t_node != remove_node:
            visited[t_node] = True
            if len(graph[t_node]) == 0:
                append_num += 1
            dfs(t_node)
        elif t_node == remove_node and len(graph[t_node]) == 1:
            append_num += 1


N = int(sys.stdin.readline())
graph, graph_list = [[] for _ in range(N)], list(map(int, sys.stdin.readline().split()))
remove_node = int(sys.stdin.readline())
visited = [False for _ in range(N)]

for idx, value in enumerate(graph_list):
    if value != -1:
        graph[value].append(idx)
    else:
        start = idx
graph[remove_node] = []
visited[start] = True
dfs(start)
print(append_num)

