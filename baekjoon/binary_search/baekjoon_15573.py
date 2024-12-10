import sys
from collections import deque


def solution():
    """ 채굴기 성능 귀납적 찍기
    idea: bisect with bfs
        - 탐색 대상/범위: 성능 배열, 1 to 백만
        - 탐색 기준: 현재 성능으로 채굴 가능한 돌맹이 개수 vs K
        - 채굴 가능 돌맹이를 어떻게 효율적으로 탐색할래?
            - bfs 도입
    question:
        - 하 bfs 한번으로 어떻게 탐색 다 하지....ㅠ

    feedback:
        - 맨 처음에 그냥 큐에 다 때려넣고 시작
        - 그리고 다른 그래프 탐색 문제처럼 연속으로 이어진 애들만 정답으로 카운트해줄 필요도 없음
    """
    # bfs func
    def bfs(limit) -> int:
        cache = 0
        q = deque([])
        visited = [[0]*M for _ in range(N)]
        for i in range(M):
            if grid[0][i] <= limit:
                cache += 1
                q.append((0,i))
                visited[0][i] = 1

        for i in range(1, N):
            if grid[i][0] <= limit:
                cache += 1
                q.append((i,0))
                visited[i][0] = 1

            if grid[i][M-1] <= limit:
                cache += 1
                q.append((i,M-1))
                visited[i][M-1] = 1
        while q:
            vy, vx = q.popleft()
            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < N and -1 < nx < M and not visited[ny][nx] and grid[ny][nx] <= limit:
                    cache += 1
                    q.append((ny,nx))
                    visited[ny][nx] = 1

        return 1 if cache >= K else 0

    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(map(int, input().split())) for _ in range(N)]

    # do bisect with bfs
    answer = 0
    l, r = 1, 10**6
    while l <= r:
        mid = (l+r) // 2
        if bfs(mid):
            r = mid - 1
            answer = mid
        else:
            l = mid + 1

    print(answer)


if __name__ == "__main__":
    solution()
