import sys
"""
[풀이 시간]
1) 00:35 ~ 01:00

[요약]
1) 주어진 트리에서 지정 노드를 삭제 했을 때 남는 리프 노드 개수 출력

[전략]
1) DFS 구현해서 지정 노드가 루트 노드인 하위 트리를 탐색
    - (원본 트리의 리프 노드 개수 - 하위 트리 리프 노드) = 정답
    - 원래 그래프 자료 구조로 바꾸는 대신 일방향 구조로 만들기
        - 그래야 리프 노드 파악하기 편해진다고 판단
"""
append_num = 0


def dfs(src, visit_list):
    visit_list[src] = True
    if len(graph[src]) == 0:
        return
    for t_node in graph[src]:
        dfs(t_node, visit_list)


def result_dfs(src, visited_list):
    global append_num
    visited_list[src] = True
    checker = len([i for i in graph[src] if not visited_list[i]])
    if checker == 0:  # 여기 조건이 추가 되어야 겠당, 그냥 단순히 0이 아니라
        append_num += 1
        return
    for t_node in graph[src]:
        if not visited_list[t_node]:
            result_dfs(t_node, visited_list)


N = int(sys.stdin.readline())
graph, graph_list,  = [[] for _ in range(N)], list(map(int, sys.stdin.readline().split()))
visited = [False for _ in range(N)]
remove_node = int(sys.stdin.readline())
for idx, value in enumerate(graph_list):
    if value != -1:
        graph[value].append(idx)

dfs(remove_node, visited)
for i in range(N):
    if not visited[i]:
        result_dfs(i, visited)
print(append_num)
