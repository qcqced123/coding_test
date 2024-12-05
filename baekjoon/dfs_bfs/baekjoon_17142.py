import sys
from collections import deque
from itertools import combinations


def sol_baekjoon_17142():
    """ solution func of baekjoon 17142
    idea: backtracking with bfs
        - 활성 바이러스 조합 뽑기
        - 조합 경우의 수마다 bfs 수행
        - 0 개수를 미리 세어주기
    feedback:
        - 비활성 바이러스 방문, 시간 처리:
            - 방문 X 방식: 비활성 바이러스 건너편에 빈 칸이 있으면, 도달할 수 없게 되어 틀림
            - 비활성 바이러스 시간 처리 x: 값 자체가 틀리게 나옴
            - 비활성 바이러스 시간 처리 0: 빈칸 없고 전부 비활성 바이러스인 경우 답이 틀림
            => 따라서, 비활성 바이러스를 만나면 시간 처리는 하되, 비활성 바이러스로부터 나오는 "시간값은 정답값 업데이트에 활용하지 않도록 만들자"
            => 이렇게 무시할 수도 있구나 싶어서... 참... 개어럽네...
    """
    INF = sys.maxsize
    input = sys.stdin.readline

    # init data structure
    N, M = map(int, input().split())
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(map(int, input().split())) for _ in range(N)]

    # get virus position list, count how many empty space in current state of grid
    virus = [(i, j) for i in range(N) for j in range(N) if grid[i][j] == 2]
    zeros = 0
    for i in range(N):
        zeros += grid[i].count(0)

    # do backtrack with bfs, combinations
    answer = INF
    for comb in combinations(virus, M):
        # do bfs
        cache = 0
        zero_cache = zeros
        q = deque([])
        visited = [[0] * N for _ in range(N)]
        for y, x in comb:
            q.append((y, x, 0))
            visited[y][x] = 1

        while q:
            vy, vx, vc = q.popleft()
            if not grid[vy][vx]:
                cache = max(cache, vc)

            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < N and -1 < nx < N and not visited[ny][nx] and grid[ny][nx] != 1:
                    nc = vc + 1
                    if not grid[ny][nx]:
                        zero_cache -= 1

                    visited[ny][nx] = 1
                    q.append((ny,nx,nc))

        if not zero_cache:
            answer = min(answer, cache)

    print(answer) if answer != INF else print(-1)


if __name__ == "__main__":
    sol_baekjoon_17142()
