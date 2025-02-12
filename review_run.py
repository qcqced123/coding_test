import sys
from collections import deque, defaultdict

INF = sys.maxsize
input = sys.stdin.readline


def solution():
    """
    insert your solution here
    """

    # bfs func
    def bfs():
        answer = 1
        visited = set()
        visited.add((1,1))
        q = deque([(1,1)])
        while q:
            vy, vx = q.popleft()
            for sy, sx in switches[(vy, vx)]:
                if not grid[sy][sx]:
                    answer += 1
                    grid[sy][sx] = 1

            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if 0 < ny < N+1 and 0 < nx < N+1 and grid[ny][nx] and (ny, nx) not in visited:
                    q.append((ny, nx))
                    visited.add((ny, nx))

            for r in range(1, N+1):
                for c in range(1, N+1):
                    if grid[r][c] and (r,c) not in visited:
                        for i in range(4):
                            nr, nc = r + dy[i], c + dx[i]
                            if 0 < nr < N+1 and 0 < nc < N+1 and grid[nr][nc] and (nr, nc) in visited:
                                q.append((r, c))
                                visited.add((r, c))
                                break
        return answer

    # get input data
    N, M = map(int, input().split())
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [[0]*(N+1) for _ in range(N+1)]

    # initialize hash
    switches = defaultdict(list)
    for _ in range(M):
        x, y, a, b = map(int, input().split())
        switches[(y,x)].append((b,a))

    # do bfs
    grid[1][1] = 1
    print(bfs())


if __name__ == '__main__':
    solution()