""" 다익스트라 = 가중치 있는 bfs
=> 최소 비용을 요구하는데 가중치가 존재한다면, 다익스트라
=> 최소 비용을 요구하는데 가중치가 모든 노드가 동일하다면 bfs
1) 자료구조: heapq
    - 이거 사용법 다시 익히자
    - 이거 정렬도 기본이 오름차순 정렬이고, 사전식으로 맨 앞 원소부터 정렬한다는 사실을 잊지 말자
    - 초기화/추가: 
        q = []
        heapq.heappush(q, (1,1,1)) 
    - 빼기
        heapq.heappop(q)

2) dist[y][x]: 시작점에서 (y,x)까지 도달하는데 필요한 최소 비용
    - 최소 비용 갱신을 못하면 그냥 방문했던 노드로 처리하고 해당 경로는 더이상 힙에 넣지 않음
        - 같은 논리로 큐에서 꺼냈을 때 한번 큐에 저장된 비용이랑 현 위치 비용이 같은지 다른지 보면, 탐색 비용을 줄일 수 있음
    - 초기화: 무조건 무한대로 해야함, 그래야 최소 비용처리하고 갱신이 되니까
    - 여기도 그리드 밖으로 나가는거 조심하고
"""
def solution1():
    """ 긴급 복구 경로 (Day 8 아침)
    
    problem:
        - 목적지까지 최소 복구 비용 구하기

    idea: dijkstra

    state:
        - board[y][x]: 해당칸 지나가는데 필요한 복구 비용
        - dist[y][x]: 출발지로부터 해당 위치까지 오는데 필요한 최소 복구 비용
        - dist[N-1][M-1]: 목적지까지 오는데 필요한 최소 복구 비용

    """
    import sys
    import heapq

    # get input
    INF = sys.maxsize
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    # direction vector
    dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

    # dijkstra func
    def dijkstra(sy: int, sx: int):
        q = []
        heapq.heappush(q, (0, sy, sx))
        dist = [[INF]*M for _ in range(N)]
        dist[sy][sx] = 0

        while q:
            c, y, x = heapq.heappop(q)

            if c != dist[y][x]:
                continue

            for d in range(4):
                ny, nx = y + dy[d], x + dx[d]

                if not (-1 < ny < N and -1 < nx < M):
                    continue

                nc = c + board[ny][nx]
                if nc < dist[ny][nx]:
                    dist[ny][nx] = nc
                    heapq.heappush(q, (nc, ny, nx))

        return dist[N-1][M-1]

    answer = dijkstra(0, 0)
    
    return answer




if __name__ == "__main__":
    print(solution1())