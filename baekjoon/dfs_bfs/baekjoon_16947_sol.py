import sys
from collections import deque
"""
[Idea]
1) 지선 대신에 순환선 부터 찾는다
    => 현재역과 시작역이 같고, 현재 2개역 이상을 지나왔다면 사이클
2) BFS + DFS
"""


def dfs(curr, src, cnt):
    """ 순환선에 해당하는 하위 그래프 찾기 """
    global cycle
    if curr == src and cnt >= 2:
        """ 현재 역과 시작 역이 같고, 2개 이상의 역을 지난 상황, 여기서 function call 종료 """
        cycle = True
        return
    visited[curr] = True
    for i in station_list[curr]:
        if not visited[i]:
            dfs(i, src, cnt + 1)
        elif i == src and cnt >= 2:
            """ 다음 방문할 역이 start node, cnt 값을 증가 시키지 않고 call, 이후 바로 첫번째 분기로 넘어가 return """
            dfs(i, src, cnt)


def bfs():
    """ 지선에 해당 되는 노선 내부 원소들의 개별 거리값 """
    global check
    queue = deque()
    for i in range(N):
        if isCycle[i]:
            check[i] = 0
            queue.append(i)
    while queue:
        curr = queue.popleft()
        for i in station_list[curr]:
            if check[i] == -1:
                queue.append(i)
                check[i] = check[curr] + 1
    for i in check:
        print(i, end=' ')
    return


sys.setrecursionlimit(1000000)
N = int(sys.stdin.readline())
station_list, start_list, check = [[] for _ in range(N+1)], [], [-1] * (N+1)
isCycle = [False] * (N+1)
# make station list
for _ in range(N):
    src, end = map(int, sys.stdin.readline().split())
    station_list[src].append(end), station_list[end].append(src)

for i in range(1, N+1):
    visited = [False] * (N+1)
    cycle = False
    dfs(i, i, 0)

    if cycle:
        isCycle[i] = True

bfs()
