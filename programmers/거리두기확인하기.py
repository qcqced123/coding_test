from collections import deque


def my_solution(places):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/81302
    """
    def bfs(y, x, graph):
        q, visit = deque(), [[0] * 5 for _ in range(5)]
        q.append((0, y, x));
        visit[y][x] = 1
        while q:
            vd, vy, vx = q.popleft()
            for i in range(4):
                nd, ny, nx = vd + 1, vy + dy[i], vx + dx[i]
                if -1 < ny < 5 and -1 < nx < 5 and nd < 3 and not visit[ny][nx]:
                    if graph[ny][nx] == 'P':
                        return 0

                    elif graph[ny][nx] == 'O':
                        q.append((nd, ny, nx)); visit[ny][nx] = 1

        return 1

    answer = []
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    cases = [[list(col) for col in place] for place in places]
    for case in cases:
        grid = case
        waiters = [(r, c) for r in range(5) for c in range(5) if grid[r][c] == 'P']
        for waiter in waiters:
            r, c = waiter
            if not bfs(r, c, grid):
                answer.append(0)
                break
        else:
            answer.append(1)

    return answer