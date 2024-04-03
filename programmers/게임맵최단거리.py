from collections import deque


def solution(maps):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/1844

    summary:
        1) 상대 팀 진영 먼저 파괴(도착)
          - 누가 더 빨리 도착하는가 == BFS

    solution:
        1) 2D Table with BFS
    """

    def bfs(y: int, x: int, graph) -> int:

        def is_goal(curr_y, curr_x):
            return curr_y == len(graph) - 1 and curr_x == len(graph[0]) - 1

        def is_valid(curr_y, curr_x):
            return -1 < curr_y < len(graph) and -1 < curr_x < len(graph[0]) and not visit[curr_y][curr_x] and \
                graph[curr_y][curr_x]

        visit, queue = [[0] * len(graph[0]) for _ in range(len(graph))], deque([(1, y, x)])  # 시간, 좌표
        visit[y][x] = 1
        while queue:
            vt, vy, vx = queue.popleft()
            for i in range(4):
                nt, ny, nx = vt + 1, vy + dy[i], vx + dx[i]
                if is_valid(ny, nx):
                    if is_goal(ny, nx):
                        return nt

                    queue.append((nt, ny, nx));
                    visit[ny][nx] = 1
        return -1

    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    answer = bfs(0, 0, maps)
    return answer

