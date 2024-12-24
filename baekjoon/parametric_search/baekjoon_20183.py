import sys
from collections import defaultdict


def solution():
    """
    idea: bfs & parametric search
        - 시작 to 도착의 최단 경로
        - 굳이 파라매트릭이 필요할까?
        - 이러면 메모리가 터지니까,

    reference:
        - https://www.acmicpc.net/board/view/115732
6 6 1 6 10
1 2 5
2 3 5
1 4 1
4 5 5
5 3 1
3 6 1
    """
    from collections import deque

    # bfs func
    def bfs(x: int, limit: int) -> int:
        answer = limit+1
        q = deque([(x, 0)])
        visited = [INF]*(N+1)
        visited[x] = 0
        while q:
            vx, vc = q.popleft()
            vp = visited[vx]
            for nc, nx in graph[vx]:
                new_cost = vc + nc
                np = max(vp, nc)
                if new_cost <= C and np < answer and np <= visited[nx]:
                    if nx == B:
                        answer = min(answer, np)
                    else:
                        visited[nx] = np
                        q.append((nx, new_cost))

        return -1 if answer == limit+1 else answer

    # get input data
    INF = sys.maxsize
    input = sys.stdin.readline
    N, M, A, B, C = map(int, input().split())  # 노드, 간선, 시작, 도착, 가진돈(limit)

    # init graph structure
    graph = defaultdict(list)
    for _ in range(M):
        src, end, cost = map(int, input().split())
        graph[src].append((cost, end)), graph[end].append((cost, src))

    # do bfs
    result = 0
    l, r = 1, int(1e+9)
    while l <= r:
        mid = (l+r) // 2
        if bfs(A, mid) != -1:
            result = mid
            r = mid - 1
        else:
            l = mid + 1

    print(result if result else -1)


def solution2():
    """
    idea: dijkstra + parametric search
    """
    import heapq

    # dijkstra func
    def dijkstra():
        h = []
        cost[A] = 0
        heapq.heappush(h, (0, A))
        while h:
            vc, vx = heapq.heappop(h)
            if vc > C:
                continue

            for nc, nx in graph[vx]:
                new_cost = vc + nc
                if nc <= mid and nc <= cost[nx] and new_cost <= C:
                    cost[nx] = nc
                    heapq.heappush(h, (new_cost, nx))

        return -1 if cost[B] == INF else cost[B]

    # get input data
    INF = sys.maxsize
    input = sys.stdin.readline
    N, M, A, B, C = map(int, input().split())  # 노드, 간선, 시작, 도착, 가진돈(limit)

    # init graph structure
    graph = defaultdict(list)
    for _ in range(M):
        src, end, cost = map(int, input().split())
        graph[src].append((cost, end)), graph[end].append((cost, src))

    # do parametric search with dijkstra
    answer = 0
    l, r = 1, int(1e+9)
    while l <= r:
        mid = (l+r) // 2
        cost = [INF]*(N+1)
        if dijkstra() != -1:
            r = mid - 1
            answer = mid
        else:
            l = mid + 1

    print(answer if answer else -1)


def solution3():
    import heapq

    # dijkstra func
    def dijkstra():
        h = []
        cost = [INF]*(N+1)
        heapq.heappush(h, (0, A))
        cost[A] = 0
        while h:
            vc, vx = heapq.heappop(h)
            for nc, nx in graph[vx]:
                new_cost = vc + nc
                if nc <= cost[B] and nc <= cost[nx] and new_cost <= C:
                    cost[nx] = nc
                    heapq.heappush(h, (new_cost, nx))

        return -1 if cost[B] == INF else cost[B]

    # get input data
    INF = sys.maxsize
    input = sys.stdin.readline
    N, M, A, B, C = map(int, input().split())  # 노드, 간선, 시작, 도착, 가진돈(limit)

    # init graph structure
    graph = defaultdict(list)
    for _ in range(M):
        src, end, cost = map(int, input().split())
        graph[src].append((cost, end)), graph[end].append((cost, src))

    # do parametric search with dijkstra
    print(dijkstra())

def solution4():
    """
    idea: dijkstra + parametric search
        - 이렇게 간선을 최적화 대상으로 세팅하면, 다익스트라에 큰 변형을 가하지 않고도, 가진 비용을 만족하면서 더 작은 수치심 값을 업데이트 가능
        - 아까는 parametric search를 안쓰고 처리하다 보니, 가진 비용 안쪽에서 더 작은 수치심의 경로를 들고 있으려고 하다보면서, 메모리가 터짐
    """
    import heapq

    # dijkstra func
    def dijkstra(limit: int) -> int:
        h = []
        cost[A] = 0
        heapq.heappush(h, (0, A))
        while h:
            vc, vx = heapq.heappop(h)
            if vc > cost[vx]:
                continue

            for nc, nx in graph[vx]:
                new_cost = nc + vc
                if nc <= limit and new_cost < cost[nx]:
                    cost[nx] = new_cost
                    heapq.heappush(h, (new_cost, nx))

        return cost[B]

    # get input data
    INF = sys.maxsize
    input = sys.stdin.readline
    N, M, A, B, C = map(int, input().split())  # 노드, 간선, 시작, 도착, 가진돈(limit)

    # init graph structure
    graph = defaultdict(list)
    for _ in range(M):
        src, end, cost = map(int, input().split())
        graph[src].append((cost, end)), graph[end].append((cost, src))

    # do parametric search with dijkstra
    answer = 0
    l, r = 1, int(1e+9)
    while l <= r:
        mid = (l+r) // 2
        cost = [INF] * (N+1)
        if dijkstra(mid) <= C:
            answer = mid
            r = mid - 1
        else:
            l = mid + 1

    print(answer if answer else -1)


if __name__ == "__main__":
    solution4()
