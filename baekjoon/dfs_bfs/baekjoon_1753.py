import sys
"""
[요약]
1) 방향 그래프가 주어지면 시작점에서 다른 모든 정점으로의 최단 경로 구하는 프로그램 작성
    - 가중치: 10이하 자연수
    - 시간 제한: 1초, 메모리 여유, 길이 2만 & 30만
    - 다익스트라... 생각이 안난다.
[전략]
1) start to all graph
    - DFS 혹은 BackTracking
    - 가중치 정보: 노드 연결 정보와 동일한 형상으로 저장
"""


def dfs(x: int, result: int = 0) -> None:
    for i in range(lent(graph[x])):
        tmp_cost = min(weights[x][i], cost[graph[x][i]])
        cost[graph[x][i]] = min(cost[graph[x][i]], result + tmp_cost)
        dfs(graph[x][i], result + tmp_cost)


sys.setrecursionlimit(10**8)
V, E = map(int, sys.stdin.readline().split())
src = int(sys.stdin.readline())

# init graph
graph, weights, cost = [[] for _ in range(V+1)], [[] for _ in range(V+1)], [float('inf')] * (V+1)
cost[src] = 0
for _ in range(E):
    u, v, weight = map(int, sys.stdin.readline().split())
    graph[u].append(v), weights[u].append(weight)  # 노드가 최대 2만개, 그래서 메모리 초과가 발생한다.

dfs(src)

for i in range(1, V+1):
    print(cost[i] if cost[i] != float('inf') else 'INF')








