import sys
from collections import deque


def solution():
    """ "연결": 육지의 상하좌우에 '다리' 존재
    idea: graph search
        - 영역별 구분 짓기
            - 현재 상태는 다른 대륙끼리 모두 값이 같아서, 구분을 지어줄 수가 없어여...

        - 다른 영역 까지 거리 카운트
            - 시간 복잡도 터질거 같은데
    question:
        - 진짜 해볼만한건 다했는데,,, 계속 39%에서 틀리거나 메모리가 터짐
    """
    def coloring(y: int, x: int, paint: int) -> None:
        grid[y][x] = paint
        q = deque([(y,x)])
        while q:
            vy, vx = q.popleft()
            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < N and -1 < nx < N and grid[ny][nx] == 1:
                    grid[ny][nx] = paint
                    q.append((ny,nx))
        return

    def cal_distance(y: int, x: int, paint: int) -> int:
        q = deque([(y,x,0)])
        visited.add((y,x))
        while q:
            vy, vx, vc = q.popleft()
            if vc >= answer:
                return -1

            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < N and -1 < nx < N:
                    if not grid[ny][nx]:
                        visited.add((ny,nx))
                        q.append((ny,nx,vc+1))

                    elif grid[ny][nx] != paint:
                        return vc
        return -1

    # init the data structure
    INF = sys.maxsize
    input = sys.stdin.readline
    N = int(input())
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(map(int, input().split())) for _ in range(N)]

    # coloring the different continent
    color = 2
    for y in range(N):
        for x in range(N):
            if grid[y][x] == 1:
                coloring(y, x, color)
                color += 1

    # find the minimum distance
    answer = INF
    visited = set()
    for c in range(2, color+1):
        for y in range(N):
            for x in range(N):
                if grid[y][x] == c:
                    cnt = cal_distance(y, x, c)
                    if cnt == -1:
                        continue
                    answer = min(answer, cnt)
                    visited.clear()
    print(answer)


def solution2():
    def coloring(y: int, x: int, paint: int) -> None:
        grid[y][x] = paint
        q = deque([(y,x)])
        while q:
            vy, vx = q.popleft()
            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < N and -1 < nx < N and grid[ny][nx] == 1:
                    grid[ny][nx] = paint
                    q.append((ny,nx))
        return

    def cal_distance(y: int, x: int, paint: int) -> int:
        q = deque([(y,x)])
        visited[y][x] = 0
        while q:
            vy, vx = q.popleft()
            vc = visited[vy][vx]
            if vc >= answer:
                return -1

            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < N and -1 < nx < N:
                    if not grid[ny][nx] and visited[ny][nx] == -1:
                        visited[ny][nx] = vc + 1
                        q.append((ny,nx))

                    elif grid[ny][nx] and grid[ny][nx] != paint:
                        return vc
        return -1

    # init the data structure
    INF = sys.maxsize
    input = sys.stdin.readline
    N = int(input())
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(map(int, input().split())) for _ in range(N)]

    # coloring the different continent
    color = 2
    for y in range(N):
        for x in range(N):
            if grid[y][x] == 1:
                coloring(y, x, color)
                color += 1

    # find the minimum distance
    answer = INF
    for c in range(2, color+1):
        for y in range(N):
            for x in range(N):
                if grid[y][x] == c:
                    visited = [[-1] * N for _ in range(N)]
                    cnt = cal_distance(y, x, c)
                    if cnt == -1:
                        continue
                    answer = min(answer, cnt)
    print(answer)


def solution3():
    def coloring(y: int, x: int, paint: int) -> None:
        grid[y][x] = paint
        q = deque([(y,x)])
        while q:
            vy, vx = q.popleft()
            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < N and -1 < nx < N and grid[ny][nx] == 1:
                    grid[ny][nx] = paint
                    q.append((ny,nx))
        return

    def cal_distance(y: int, x: int, paint: int) -> int:
        q = deque([(y,x)])
        while q:
            vy, vx = q.popleft()
            if grid[vy][vx] > 0:
                vc = 0

            else:
                vc = abs(grid[vy][vx])
                if vc >= answer:
                    return -1

            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < N and -1 < nx < N:
                    curr = -(vc + 1)
                    if curr < grid[ny][nx] <= 0:
                        grid[ny][nx] = curr
                        q.append((ny, nx))

                    elif grid[ny][nx] > 0 and grid[ny][nx] != paint:
                        return vc
        return -1

    # init the data structure
    INF = sys.maxsize
    input = sys.stdin.readline
    N = int(input())
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    grid = [list(map(int, input().split())) for _ in range(N)]

    # coloring the different continent
    color = 2
    for y in range(N):
        for x in range(N):
            if grid[y][x] == 1:
                coloring(y, x, color)
                color += 1

    # find the minimum distance
    answer = INF
    for c in range(2, color+1):
        for y in range(N):
            for x in range(N):
                if grid[y][x] == c:
                    cnt = cal_distance(y, x, c)
                    if cnt == -1:
                        continue
                    answer = min(answer, cnt)
    print(answer)


def solution4():
    def coloring(y: int, x: int, paint: int) -> None:
        grid[y][x] = paint
        q = deque([(y,x)])
        color_visited[y][x] = 1
        while q:
            vy, vx = q.popleft()
            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < N and -1 < nx < N and not color_visited[ny][nx] and grid[ny][nx] == 1:
                    grid[ny][nx] = paint
                    q.append((ny,nx))
                    color_visited[ny][nx] = 1
        return

    def cal_distance(paint: int) -> int:
        q = deque([])
        visited = [[-1] * N for _ in range(N)]
        for y in range(N):
            for x in range(N):
                if grid[y][x] == paint:
                    q.append((y, x))
                    visited[y][x] = 0
        while q:
            vy, vx = q.popleft()
            vc = visited[vy][vx]
            if vc >= answer:
                return INF

            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < N and -1 < nx < N:
                    if not grid[ny][nx] and visited[ny][nx] == -1:
                        visited[ny][nx] = vc + 1
                        q.append((ny, nx))

                    elif grid[ny][nx] and grid[ny][nx] != paint:
                        return vc
        return INF

    # init the data structure
    INF = sys.maxsize
    input = sys.stdin.readline
    N = int(input())
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    color_visited = [[0]*N for _ in range(N)]
    grid = [list(map(int, input().split())) for _ in range(N)]

    # coloring the different continent
    color = 2
    for y in range(N):
        for x in range(N):
            if grid[y][x] == 1 and not color_visited[y][x]:
                coloring(y, x, color)
                color += 1

    # find the minimum distance
    answer = INF
    for c in range(2, color+1):
        answer = min(answer, cal_distance(c))

    print(answer)


if __name__ == "__main__":
    solution4()
