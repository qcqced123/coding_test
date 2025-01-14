import sys
from collections import deque


def solution():
    """
    idea: parametric search + bfs
        - 최적화 대상/범위: 레벨, 0 to max(grid[i][j])
        - 최적화 기준: grid[i][j] > mid => 이 케이스가 1번 이하인가

    question/result:
        - 2% 틀림... 왜...? 아니 왜...?

    feedback:
        - 애초에 특수 장비 사용 조건부터 제대로 안 읽고 구현함, 그니까 틀리지
    """
    # bfs func
    def bfs(limit: int) -> int:
        visited = set()
        visited.add((0,0))
        count = 0 if limit >= grid[0][0] else 1
        q = deque([(0,0,count)])
        while q:
            vy, vx, vc = q.popleft()
            for i in range(4):
                ny, nx, nc = vy + dy[i], vx + dx[i], vc
                if -1 < ny < n and -1 < nx < m and (ny, nx) not in visited:
                    if grid[ny][nx] > limit:
                        nc += 1

                    if nc < 2:
                        if ny == n-1 and nx == m-1:
                            return 1

                        visited.add((ny,nx))
                        q.append((ny,nx,nc))
        return 0

    # get input data
    INF = sys.maxsize
    input = sys.stdin.readline
    n, m = map(int, input().split())
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(map(int, input().split())) for _ in range(n)]

    # do parametric search with bfs
    answer = INF
    l, r = INF, 0
    for i in range(n):
        l = min(l, min(grid[i]))
        r = max(r, max(grid[i]))

    while l <= r:
        mid = (l+r) // 2
        if bfs(mid):
            answer = mid
            r = mid - 1

        else:
            l = mid + 1

    print(answer)


if __name__ == "__main__":
    solution()
