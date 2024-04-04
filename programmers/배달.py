import heapq
from collections import defaultdict


def solution(N, road, K):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/12978

    summary:
        1) N개의 마을
          - 노드 번호는 1~N
          - 양방향 간선
          - 시작 위치: 1번

    return:
        k시간 이하 걸리는 위치까지만 배달, 배달 가능한 곳 세어서 스칼라 리턴

    solution:
        1) 다익스트라
    """
    graph, distance = defaultdict(list), [float('inf')] * (N + 1)
    for node_info in road:
        src, end, cost = node_info
        graph[src].append((cost, end)), graph[end].append((cost, src))

    def dijkstra(x: int) -> None:
        h = []
        distance[x] = 0
        heapq.heappush(h, [distance[x], x])
        while h:
            min_cost, node = heapq.heappop(h)
            if min_cost > distance[node]:
                continue

            for candidate in graph[node]:
                curr_cost, curr_node = candidate
                new_cost = curr_cost + min_cost
                if new_cost < distance[curr_node]:
                    distance[curr_node] = new_cost
                    heapq.heappush(h, [new_cost, curr_node])

    dijkstra(1)
    answer = len([time for time in distance[1:] if time <= K])
    return answer