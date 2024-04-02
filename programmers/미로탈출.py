from collections import deque


def solution(maps):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/159993

    summary:
        1) 직사각형 미로 탈출
          - 레버 당긴 이후, 탈출 가능
        => 최단 시간으로 미로 빠져나가는 시간
    """
    def bfs(y: int, x: int, target: str, graph):
        visit, q = set(), deque([])
        visit.add((y, x)), q.append((0, y, x))
        while q:
            vt, vy, vx = q.popleft()
            for i in range(4):
                nt, ny, nx = vt + 1, vy + dy[i], vx + dx[i]
                if -1 < ny < len(graph) and -1 < nx < len(graph[0]) and (ny, nx) not in visit:
                    if graph[ny][nx] == target:
                        return nt

                    elif graph[ny][nx] == 'O':
                        visit.add((ny, nx));
                        q.append((nt, ny, nx))
        return 0

    grid = []
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    sy, sx, ly, lx, ey, ex = 0, 0, 0, 0, 0, 0  # 시작, 레버, 끝
    for r in range(len(maps)):
        col = maps[r]
        grid.append(list(col))
        for c in range(len(col)):
            if col[c] == "S":
                sy, sx = r, c
            elif col[c] == "L":
                ly, lx = r, c
            elif col[c] == "E":
                ey, ex = r, c

    flag = False
    grid[sy][sx] = 'O'
    if not flag: grid[ey][ex] = 'O'

    curr = bfs(sy, sx, 'L', grid)
    if curr: flag = True

    if flag:
        grid[ey][ex] = 'E'
        tmp = bfs(ly, lx, 'E', grid)

    answer = curr + tmp if curr and tmp else -1
    return answer

