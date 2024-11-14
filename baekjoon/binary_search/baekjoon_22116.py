import sys
import heapq
from collections import deque, defaultdict


def solution():
    """ 인접 행렬 탐색, 상하좌우, 최대  경사의 최소값,
    경사: 인접한 격자 사이의 높이 차이의 절대값
    비용: 비용 높을수록 높은 경사를 올라갈 수 있음

    idea: binary search
        값이 10억인걸 봐서, 이분탐색
        - 시작 to 목적까지 경로를 계산하고 가면서, 경로들의 높이차이가 가장 작은
        - 탐색 대상/범위: 경사값 배열, 1 to 10억
        - 탐색 조건:
        - 탐색 알고리즘:
            - bfs or dfs with binary search
    question:
        - bfs with adj array: N**2 => 백만
        - binary search => 1만
            => 최종 100억
            => 이러니 안되지
    """

    # bfs search
    def bfs(y: int, x: int, limit: int) -> int:
        # init the queue, visited array
        q = deque([(y, x)])
        visited = [[0] * N for _ in range(N)]
        visited[y][x] = 1
        while q:
            vy, vx = q.popleft()
            # end point of bfs search, if we can find the minimum path
            if vy == N - 1 and vx == N - 1:
                return 1

            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < N and -1 < nx < N:
                    is_movable = abs(grid[vy][vx] - grid[ny][nx])  # for bisect
                    if not visited[ny][nx] and is_movable <= limit:
                        q.append((ny, nx))
                        visited[ny][nx] = 1
        return 0

    # init the data structure
    input = sys.stdin.readline
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # do bisect
    answer = 0
    l, r = 0, 1000000000
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    while l <= r:
        mid = (l + r) // 2
        if bfs(0, 0, mid):
            answer = mid
            r = mid - 1

        else:
            l = mid + 1

    print(answer)


def solution2():
    """ NlogN * MlogM (1만 * 1만)
    그래프 탐색 중에 NlogN 짜리가...? 다익스트라...?
    idea 2: dijkstra with binary search
        - bfs를 다익스트라로 변경
        - 나머지 논리 구조 동일

    question:
        - 왜 또 시간초과ㅑ..
        - 그냥 계속 시간초과...
    """
    # dijkstra search
    def dijkstra(y: int, x: int, limit: int) -> int:
        h = []
        visited[(y, x)] = 0
        heapq.heappush(h, (0, y, x))
        while h:
            vl, vy, vx = heapq.heappop(h)  # for the minimum
            if vl > visited[(vy, vx)]:
                continue

            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < N and -1 < nx < N:
                    nl = abs(grid[vy][vx] - grid[ny][nx])
                    if nl <= limit and nl < visited[(ny, nx)]:
                        visited[(ny, nx)] = nl
                        heapq.heappush(h, (nl, ny, nx))

        if visited[(N-1, N-1)] != INF: return 1
        else: return 0

    # init the data structure
    INF = sys.maxsize
    input = sys.stdin.readline
    N = int(input())
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(map(int, input().split())) for _ in range(N)]

    # do bisect
    answer = 0
    l, r = 0, 1000000000
    while l <= r:
        mid = (l+r) // 2
        visited = defaultdict(lambda: INF)
        if dijkstra(0, 0, mid):
            answer = mid
            r = mid - 1

        else:
            l = mid + 1

    print(answer)


def solution3():
    """ 생각해보면 다익스트라에 굳이 이진 탐색을 같이 쓸 필요가 없구나
    경로 업데이트 할떄도, max(vl, abs()) 해줘야 정확함
    왜냐 더 큰 값을 들고 있어야, 현재 경로 상의 가장 큰 경사가 계속 보존되기 때문, 저게 없으면, 작은값이 현재 경로의 가장 큰 경사처럼 둔갑함
    """
    # dijkstra search
    def dijkstra(y: int, x: int) -> int:
        h = []
        visited[y][x] = 0
        heapq.heappush(h, (0, y, x))
        while h:
            vl, vy, vx = heapq.heappop(h)  # for the minimum
            if vl > visited[vy][vx]:
                continue

            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < N and -1 < nx < N:
                    nl = max(vl, abs(grid[vy][vx] - grid[ny][nx]))  # 이렇게 해야, 경로 상 가장 큰 경사가 계속 보존 된다, 이걸 빼먹었구나, 잘 구현했네
                    if nl < visited[ny][nx]:
                        visited[ny][nx] = nl
                        heapq.heappush(h, (nl, ny, nx))

        return visited[N-1][N-1]

    # init the data structure
    INF = sys.maxsize
    input = sys.stdin.readline
    N = int(input())
    visited = [[INF]*N for _ in range(N)]
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(map(int, input().split())) for _ in range(N)]
    print(dijkstra(0, 0))

    return


if __name__ == "__main__":
    solution3()
