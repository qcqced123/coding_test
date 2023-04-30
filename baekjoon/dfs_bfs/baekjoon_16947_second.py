import sys
"""
[풀이 시간]
1) 21:20 ~ 22:20

[요약]
1) 역 A와 순환선 사이의 거리는 A와 순환선에 속하는 역 사이의 거리 중 최솟값
    - 노선도가 주어졌을 때, 주어진 역과 순환선 사이의 거리 구하기
    - 즉, 현재 연산 하려는 역이 순환선이건 지선이건 상관없이 순환선과의 거리를 구해야 함
[전략]
1) 해당 역으로부터 특정 노드까지의 거리를 구해야 하기 때문에 DFS 구현
    - 시작 노드 번호가 1이기 때문에 맞춰서 인덱스 구현
2) 시작 노드를 어떻게 지선으로 잡아줄 것인가
    - station_list 길이가 1인 애들이 아마도 지선의 시작 지점
3) 해당 노드가 어떻게 순환선에 해당하는지 판단할 것인가
    - 그렇 다면 길이가 3이상인 노드에 대해서 순환선 인지 판정 하는 코드를 넣어보자
    - 자기 자신이 포함된 리스트를 다시 만날 수 있나 없나로 판정해야 할 것 같음
"""


def dfs(x, visited, distance):
    global count
    visited[x] = True
    for new in station_list[x]:
        if not visited[new] and len(station_list[new]) == 2:
            """ keep dfs """
            dfs(new, visited, distance)

        elif not visited[new] and len(station_list[new]) >= 3:
            """ check for cycle """
            dfs(new, visited, distance)
    distance[x] = count
    count += 1


sys.setrecursionlimit(1000000)
N = int(sys.stdin.readline())
station_list, start_list, result_list = [[] for _ in range(N+1)], [], [0] * (N+1)

for _ in range(N):
    src, end = map(int, sys.stdin.readline().split())
    station_list[src].append(end), station_list[end].append(src)

for i in range(1, N+1):
    if len(station_list[i]) == 1:
        start_list.append(i)

for src in start_list:
    count = 0
    visited_list = [False] * (N+1)
    dfs(src, visited_list, result_list)

