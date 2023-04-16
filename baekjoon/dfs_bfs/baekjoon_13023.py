import sys
"""
[풀이 시간]
1) 21:40 ~ 22:10

[요약]
1) A->B, B->C, C->D, D->E
    - 위와 같은 친구 관계를 가진 집단이 존재 하는지 판단
[전략]
1) 시간 & 메모리 충분함
2) 총 탐색 횟수가 5인 트리가 몇 개일까 찾는 문제

=> Python Recursion 동작에 대해서 다시 공부할 수 있었던 좋은 문제
"""


def dfs(src, path_list):
    # print(path_list)
    if len(path_list) == 5:
        print(1)
        exit()

    if src not in path_list:
        path_list.append(src)
    else:
        return
    for t_node in graph[src]:
        dfs(t_node, path_list)
    """ Recursion은 return을 만나면 Recursion이 실행 되었던 위치의 다음 라인으로 돌아온다 """
    path_list.pop()


N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    node1, node2 = map(int, sys.stdin.readline().split())
    graph[node1].append(node2), graph[node2].append(node1)

for i in range(N):
    path = []
    dfs(i, path)
print(0)

