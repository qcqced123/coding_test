import sys
from collections import deque


def solution2():
    """
    idea1: dfs with backtracking
        - 시간 초과

    idea2: bfs with dynamic programming
        - 논리는 solution 1과 동일
        - if not visited or current walls lower than current index
    """
    # init data structure
    C, R = map(int, input().split())  # 열, 행
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(map(str, input().rstrip())) for _ in range(R)]
    visited = [[-1] * C for _ in range(R)]

    # do bfs
    visited[0][0] = 0

    queue = deque([(0, 0, 0)])
    while queue:
        vy, vx, vw = queue.popleft()  # y, x, walls
        for i in range(4):
            ny, nx = vy + dy[i], vx + dx[i]
            if -1 < ny < R and -1 < nx < C:
                cnt = visited[ny][nx]
                nw = vw + 1 if grid[ny][nx] == "1" else vw
                if cnt == -1 or nw < cnt:
                    visited[ny][nx] = nw
                    queue.append((ny,nx,nw))

    print(visited[-1][-1])


if __name__ == "__main__":
    solution2()
