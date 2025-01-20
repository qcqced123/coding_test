import sys
from collections import deque


def solution():
    """
    idea: parametric search + bfs
        - 최적화 대상/범위: 레벨, grid[0][0] to max(grid[i][j])
        - 최적화 기준: grid[i][j] > mid => 이 케이스가 1번 이하인가
    feedback:
        - 애초에 특수 장비 사용 조건부터 제대로 안 읽고 구현함, 그니까 틀리지
            - 특수 장비 사용하고, 그 다음 방향만 고정되도록 만들기!
            - 몰겠... 답지를 봅시다
    """

    # bfs func
    def bfs(limit: int) -> int:
        visited = set()
        visited.add((0, 0))
        q = deque([(0, 0, 0)])
        while q:
            vy, vx, vc = q.popleft()
            for i in range(4):
                ny, nx, nc = vy + dy[i], vx + dx[i], vc
                if -1 < ny < n and -1 < nx < m and (ny, nx) not in visited:
                    if grid[ny][nx] > limit:
                        ny += dy[i]
                        nx += dx[i]
                        if -1 < ny < n and -1 < nx < m and (ny, nx) not in visited and grid[ny][nx] <= limit:
                            nc += 1

                        else:
                            continue

                    if nc < 2:
                        if ny == n-1 and nx == m-1:
                            return 1

                        visited.add((ny, nx))
                        q.append((ny, nx, nc))
        return 0

    # get input data
    INF = sys.maxsize
    input = sys.stdin.readline
    n, m = map(int, input().split())
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(map(int, input().split())) for _ in range(n)]

    # do parametric search with bfs
    answer = max(grid[0][0], grid[-1][-1])
    l, r = answer, 0
    for i in range(n):
        r = max(r, max(grid[i]))

    while l <= r:
        mid = (l + r) // 2
        if bfs(mid):
            answer = mid
            r = mid - 1

        else:
            l = mid + 1

    print(answer)


def solution2():
    """
    idea: bfs with 3d visited cache
        - 모든 "가능한" 경로 구하기
        - 경로 중에서 최대의 최소 구하기

    question:
        - 사람들은 어떻게 parametric search를 안하고 "최대의 최소"를 최적화 했을까??
            - 그냥 모든 "가능한" 경로를 구하고, 거기서 최대값의 최소를 구했을까??
            - 아니 근데 그럼 점프 한다는 기준은 어떻게 잡을까??
            - 그 기준을 잡아야 해서 나는 파라매트릭 서치가 반드시 필요하다고 생각했는데??
            => 벽 부수는 문제도 내가 기를 쓰고 3차원 안쓰려다가 계속 틀려서, 결국 3차원 썼구나
    feedback:
        - 3차원 캐시 쓰는 문제 왜이리 못하지...ㅜ
    """
    # bfs func
    def bfs(y: int, x: int) -> int:
        q = deque([(y, x, 0)])  # index of grid, count of using jump
        visited[y][x][0] = grid[y][x]
        while q:
            vy, vx, vc = q.popleft()
            vl = visited[vy][vx][vc]
            for i in range(4):
                ny, nx, nc = vy + dy[i], vx + dx[i], vc
                if -1 < ny < n and -1 < nx < m:
                    nl = max(vl, grid[ny][nx])
                    if nl < visited[ny][nx][nc]:
                        q.append((ny, nx, nc))
                        visited[ny][nx][nc] = nl

                    if not nc:
                        ny += dy[i]
                        nx += dx[i]
                        if -1 < ny < n and -1 < nx < m:
                            nc += 1
                            nl = max(vl, grid[ny][nx])
                            if nl < visited[ny][nx][nc]:
                                q.append((ny,nx,nc))
                                visited[ny][nx][nc] = nl

        return min(visited[n-1][m-1])


    # get input data
    # init data structure
    INF = sys.maxsize
    input = sys.stdin.readline
    n, m = map(int, input().split())
    dy, dx = (-1,1,0,0), (0,0,-1,1)
    visited = [[[INF, INF] for _ in range(m)] for _ in range(n)]
    grid = [list(map(int, input().split())) for _ in range(n)]

    # do bfs
    print(bfs(0,0))


if __name__ == "__main__":
    solution2()
