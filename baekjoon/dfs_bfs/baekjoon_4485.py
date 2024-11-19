import sys
from collections import deque


def solution():
    """ 최소 금액으로 목적지 가기
    idea: bfs or dfs with dynamic programming
        - 이동 하면서 계속 캐시의 원소를 최소값 으로 갱신
        - 방문 했어도, 갱신가능하면 방문하도록 만들어서 bfs 수행
    feedback:
        - 메모리 터짐
    """
    # init the data structure
    input = sys.stdin.readline
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    checker = 1
    while True:
        N = int(input())
        if not N:
            return

        visited = [[-1]*N for _ in range(N)]  # 캐시값은 방문 배열에 기록
        grid = [list(map(int, input().split())) for _ in range(N)]

        # do the bfs
        def bfs():
            q = deque([(0, 0)])
            visited[0][0] = grid[0][0]
            while q:
                vy, vx = q.popleft()
                vc = visited[vy][vx]
                for i in range(4):
                    ny, nx = vy + dy[i], vx + dx[i]
                    if -1 < ny < N and -1 < nx < N and (visited[ny][nx] == -1 or vc + grid[ny][nx] < visited[ny][nx]):
                        nc = vc + grid[ny][nx]
                        visited[ny][nx] = nc
                        q.append((ny, nx))

        bfs()
        print(f"Problem {checker}: {visited[-1][-1]}")  # 아니 멍충아 출력 형식때문에 틀리냐
        checker += 1


if __name__ == "__main__":
    solution()
