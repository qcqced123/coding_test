import sys
import heapq
from collections import deque, defaultdict


def solution():
    """ 무향 그래프, 최소 방문 경로, NlogN....
    idea: bfs
        - init graph
        - do bfs

    question/result:
        - N == max(100000), 메모리가 터짐....
    """
    # bfs func
    def bfs(x: int) -> int:
        visited = set()
        visited.add(x)
        q = deque([(x, 1)])
        while q:
            vx, vc = q.popleft()
            for nx in graph[vx]:
                if nx == N:
                    return vc+1

                if nx not in visited:
                    visited.add(nx)
                    q.append((nx, vc+1))

        return -1

    # get input data
    input = sys.stdin.readline
    N, K, M = map(int, input().split())
    graph = defaultdict(set)

    # init graph structure
    for _ in range(M):
        cnt = list(map(int, input().split()))
        for i in range(K):
            curr = cnt[:i] + cnt[i+1:]
            for j in curr:
                graph[cnt[i]].add(j)

    # do bfs
    print(bfs(1))


def solution2():
    """
    idea: bfs + dijkstra
        - 방문 기준을 다익스트라처럼 비용 기준 사용
        - 그래도 메모리가 터지는데
    """
    # bfs func
    def bfs(x: int):
        h = []
        cost = [INF]*(N+1)
        cost[x] = 1
        heapq.heappush(h, (1, x))
        while h:
            vc, vx = heapq.heappop(h)
            if vc > cost[vx]:
                continue

            for nx in graph[vx]:
                nc = vc + 1
                if nx == N:
                    return nc

                if nc < cost[nx]:
                    cost[nx] = nc
                    heapq.heappush(h, (nc, nx))
        return -1


    # get input data
    INF = sys.maxsize
    input = sys.stdin.readline
    N, K, M = map(int, input().split())
    graph = defaultdict(set)

    # init graph structure
    for _ in range(M):
        cnt = list(map(int, input().split()))
        for i in range(K):
            curr = cnt[:i] + cnt[i+1:]
            for j in curr:
                graph[cnt[i]].add(j)
    # do bfs
    print(bfs(1))


def solution3():
    """
    idea: bfs + re-define the adj graph structure
        - 하이퍼 튜브도 노드 취급
        - 실제 노드의 연결 정보 리스트에는 해당 노드가 속하는 하이퍼 튜브의 번호를 넣고
        - 하이퍼 튜브의 연결 정보 리스트에는 해당 튜브에 속하는 노드들의 번호를 넣기

    question:
        - 하이퍼 튜브를 노드에 포함 시키는데 왜 메모리가 안터지게 될까
            - 튜브도 visited에 포함시키기 때문에 튜브 전체에 속한 노드를 방문할 이유가 사라져서??
            - 근데 개별 노드도 visited에 방문처리를 하는데, 뭐가 달라질까??
            => 예상하기로는, 연결 정보를 하이퍼튜브 노드에 몰아두니까, 일반 무향 그래프보다 중복되는 간선 정보가 줄어들어서 그렇지 않을까??
    """
    # bfs func
    def bfs(x: int) -> int:
        visited = set()
        visited.add(x)
        q = deque([(x,1)])
        while q:
            vx, vc = q.popleft()
            for nx in graph[vx]:
                nc = vc
                if nx == N:
                    return nc + 1

                if nx not in visited:
                    if nx <= N: nc += 1
                    visited.add(nx)
                    q.append((nx, nc))
        return -1

    # get input data
    INF = sys.maxsize
    input = sys.stdin.readline
    N, K, M = map(int, input().split())
    graph = defaultdict(list)

    # init graph structure
    for i in range(1, M+1):
        cnt = list(map(int, input().split()))
        for j in cnt:
            graph[j].append(N+i)
            graph[N+i].append(j)

    # do bfs
    # exception handling for N == 1
    print(bfs(1) if N > 1 else 1)

if __name__ == "__main__":
    solution3()
