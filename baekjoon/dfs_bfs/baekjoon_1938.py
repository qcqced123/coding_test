import sys
from collections import deque


def solution():
    """
    idea: bfs + prefix sum (2d table)
        - find the starting point and end point
        - init and update the prefix table
        - do bfs
            - 회전 구현 어떻게 할거야??
            - if current direction is rotate, validate the next area
    feedback:
        - visited 구현을 통나무 구성하는 좌표 조합으로 해야 하는데, 통나무 끝부분만 넣어서, 중복이 아닌데 중복 처리하게 되어 틀림

    reference:
        - https://www.acmicpc.net/board/view/22503
    """
    # helper func
    def is_valid(y1, x1, y2, x2) -> int:
        validation = prefix[y2+1][x2+1] - prefix[y1][x2+1] - prefix[y2+1][x1] + prefix[y1][x1]
        return 1 if not validation else 0

    def bfs() -> int:
        visited = set()
        q = deque([(src_point, 0)])
        visited.add(tuple(src_point))
        while q:
            vp, vc = q.popleft()
            for i in range(5):
                cnt = []
                # handling the case of rotation
                if i == 4:
                    fy, fx = vp[0]
                    sy, sx = vp[1]
                    ty, tx = vp[2]

                    if sy-fy == 1:  # 통나무 방향 == 가로
                        cnt.append((fy+1, fx-1))
                        cnt.append((sy, sx))
                        cnt.append((ty-1, tx+1))
                    else:  # 통나무 방향 == 세로
                        cnt.append((fy+1, fx+1))
                        cnt.append((sy, sx))
                        cnt.append((ty-1, tx-1))

                # handling the other case of direction
                else:
                    for j in range(3):
                        vy, vx = vp[j]
                        ny, nx = vy + dy[i], vx + dx[i]
                        cnt.append((ny,nx))

                for j in range(3):
                    ny, nx = cnt[j]
                    if not (-1 < ny < N and -1 < nx < N):
                        break
                else:
                    cnt.sort()
                    if i == 4:
                        cy, cx = cnt[1]
                        y1, x1 = cy-1, cx-1
                        y2, x2 = cy+1, cx+1
                    else:
                        y1, x1 = cnt[0]
                        y2, x2 = cnt[2]

                    if tuple(cnt) not in visited and is_valid(y1, x1, y2, x2):
                        # if bfs can find the end point
                        for i,j in cnt:
                            if (i,j) not in end_point:
                                break

                        else: return vc + 1
                        visited.add(tuple(cnt))
                        q.append((cnt, vc + 1))
        return 0

    # get the input data
    input = sys.stdin.readline
    N = int(input())
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(map(str, input().rstrip())) for _ in range(N)]

    # find the starting point and end point
    src_point, end_point = [], set()
    for i in range(N):
        for j in range(N):
            if grid[i][j] == "B":
                src_point.append((i,j))
                grid[i][j] = 0

            elif grid[i][j] == "E":
                end_point.add((i,j))
                grid[i][j] = 0

            else:
                grid[i][j] = int(grid[i][j])

    # init and update the prefix table
    prefix = [[0]*(N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + grid[i-1][j-1]

    # do bfs and return the result
    print(bfs())


if __name__ == "__main__":
    solution()
