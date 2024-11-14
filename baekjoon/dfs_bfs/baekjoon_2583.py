import sys
from collections import deque


def solution():
    """ 영역별 넓이 구하기
    idea: bfs or dfs
        - 직사격형 영역 방문 처리
        - 분할 영역 넓이 계산
        - 오름차순 정렬 및 출력

    feedback:
        - 직사각형 영역 칠할 떄, 굳이 bfs 쓸 필요 없음

    [좋은 반례]:
    4 4 1
    0 0 1 1
    answer = 15

    """
    input = sys.stdin.readline
    M, N, K = map(int, input().split())
    grid = [[0]*N for _ in range(M)]
    points = [tuple(map(int, input().split())) for _ in range(K)]  # point of each rectangle

    # record visited with bfs
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    for ldx, ldy, rux, ruy in points:
        # init start
        visited = set()
        visited.add((0,0))
        rectangle_q = deque([(0,0)])

        while rectangle_q:
            vy, vx = rectangle_q.popleft()
            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < M and -1 < nx < N and (ny, nx) not in visited:
                    if ldy <= ny < ruy and ldx <= nx < rux and not grid[ny][nx]:
                        grid[ny][nx] = 1

                    visited.add((ny, nx))
                    rectangle_q.append((ny, nx))

    # calculate the area of remain rectangle
    def cal_area(y: int, x: int) -> int:
        result = 1
        visited.add((y,x))
        q = deque([(y,x)])
        while q:
            vy, vx = q.popleft()
            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < M and -1 < nx < N and (ny, nx) not in visited and not grid[ny][nx]:
                    result += 1
                    visited.add((ny, nx))
                    q.append((ny, nx))
        return result

    area = []
    visited = set()
    for y in range(M):
        for x in range(N):
            if not grid[y][x] and (y,x) not in visited:
                area.append(cal_area(y, x))

    for i in range(M):
        print(grid[i], end='\n')


    area.sort()
    answer = len(area)
    print(answer)
    print(*area)


def solution2():
    """
    idea2: bfs

    feedback:
        - 진짜 멍청력 MAX
            - 도대체 왜 영역 칠하는데 bfs 쓸 생각을 한거지??
            - 닭 잡는데 소잡는 칼 쓰지 말자
    """
    input = sys.stdin.readline
    M, N, K = map(int, input().split())
    grid = [[0] * N for _ in range(M)]
    points = [tuple(map(int, input().split())) for _ in range(K)]  # point of each rectangle
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

    # record the rectangle
    for ldx, ldy, rux, ruy in points:
        for y in range(M):
            for x in range(N):
                if ldy <= y < ruy and ldx <= x < rux and not grid[y][x]:
                    grid[y][x] = 1

    # calculate the area of remain rectangle
    def cal_area(y: int, x: int) -> int:
        result = 1
        visited.add((y, x))
        q = deque([(y, x)])
        while q:
            vy, vx = q.popleft()
            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]
                if -1 < ny < M and -1 < nx < N and (ny, nx) not in visited and not grid[ny][nx]:
                    result += 1
                    visited.add((ny, nx))
                    q.append((ny, nx))
        return result

    area = []
    visited = set()
    for y in range(M):
        for x in range(N):
            if not grid[y][x] and (y, x) not in visited:
                area.append(cal_area(y, x))

    area.sort()
    answer = len(area)
    print(answer)
    print(*area)


if __name__ == "__main__":
    solution2()
