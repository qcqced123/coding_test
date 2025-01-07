import sys
import heapq
from collections import defaultdict


def solution():
    """
    idea: dijkstra
        - 일반 다익스트라 수행 + 경로 저장
        - 다익스트라 1번 돌리고, 주어진 목적지 후보군 중에서 경유지를 거치는 친구들을 정답에 담아주기

    question:
        - 왜 틀릴까??

    reference:
        - https://frog-in-well.tistory.com/68
        - https://www.acmicpc.net/board/view/119032
    """
    # dijkstra func
    def dijkstra(src: int) -> None:
        h = []
        cost[src] = 0
        path[src] += str(src)
        heapq.heappush(h, (0, src))
        while h:
            vc, vx = heapq.heappop(h)
            vp = path[vx]
            if vc > cost[vx]:
                continue

            for nc, nx in graph[vx]:
                new_cost = nc+vc
                if new_cost <= cost[nx]:
                    cost[nx] = new_cost
                    path[nx] = vp+str(nx)
                    heapq.heappush(h, (new_cost, nx))

    # get input data
    INF = int(10**9)
    input = sys.stdin.readline
    for _ in range(int(input())):
        graph = defaultdict(list)
        n, m, t = map(int, input().split())  # node, edge, candidates of end point
        s, g, h = map(int, input().split())  # starting point, middle point of total path

        # init graph, cost array
        for _ in range(m):
            a, b, d = map(int, input().split())  # src, end, cost
            graph[a].append((d, b)), graph[b].append((d, a))

        # init candidate array
        candidates = [int(input()) for _ in range(t)]
        candidates.sort()

        # do find the shortest path by using dijkstra
        cost = [INF]*(n+1)
        path = [""]*(n+1)
        dijkstra(s)

        # find the given hint edge in shortest path
        answer = []
        hint1, hint2 = f"{g}{h}", f"{h}{g}"
        for candidate in candidates:
            if (hint1 in path[candidate]) or (hint2 in path[candidate]):
                answer.append(candidate)

        answer.sort()
        print(*answer)


def solution2():
    """
    idea: dijkstra
        - s, g, h를 각각 시작 위치로 다익스트라 3번 수행
        - case 1. s to t == (s to g) + (g to h) + (h to t)
        - case 2. s to t == (s to h) + (h to g) + (g to t)

    reference:
        - https://frog-in-well.tistory.com/68
    """
    # dijkstra func
    def dijkstra(src: int) -> list[int]:
        h = []
        cost = [INF]*(n+1)
        cost[src] = 0
        heapq.heappush(h, (0, src))
        while h:
            vc, vx = heapq.heappop(h)
            if vc > cost[vx]:
                continue
            for nc, nx in graph[vx]:
                new_cost = nc + vc
                if new_cost < cost[nx]:
                    cost[nx] = new_cost
                    heapq.heappush(h, (new_cost, nx))
        return cost

    # get input data
    INF = int(10**9)
    input = sys.stdin.readline
    for _ in range(int(input())):
        graph = defaultdict(list)
        n, m, t = map(int, input().split())  # node, edge, candidates of end point
        s, g, h = map(int, input().split())  # starting point, middle point of total path

        # init graph, cost array
        for _ in range(m):
            a, b, d = map(int, input().split())  # src, end, cost
            graph[a].append((d, b)), graph[b].append((d, a))

        # init candidate array
        candidates = [int(input()) for _ in range(t)]
        candidates.sort()

        # do dijkstra for finding shortest path
        first_cost = dijkstra(s)
        second_cost = dijkstra(g)
        third_cost = dijkstra(h)

        # answering the question
        answer = []
        for candidate in candidates:
            total = first_cost[candidate]
            path1 = first_cost[g] + second_cost[h] + third_cost[candidate]
            path2 = first_cost[h] + third_cost[g] + second_cost[candidate]
            if total == path1 or total == path2:
                answer.append(candidate)

        print(*answer)


if __name__ == "__main__":
    solution2()
