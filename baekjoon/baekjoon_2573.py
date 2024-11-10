import sys
from collections import deque


def solution():
    """ 최초 한덩이 빙산이 두덩이가 되는 시점 구하기, N**2
    시간 복잡도가 남아 돌아서, 카피해도 괜찮을듯..?

    idea: dfs or bfs, graph
        - 빙산 녹이기 함수
            - 녹이기: 모든 빙산이 동시에 녹아야 함
            - 가중치: 동, 서, 남, 북에 바다 개수만큼 감소
            - visited 배열은 어떻게 할래..?
                - 0 이 아니면서, 기존 값이랑 달라졌을 떄, 방문한걸로 쳐야 되는데
        - 빙산 개수 카운트 함수
    """
    # init data structure
    input = sys.stdin.readline
    R, C = map(int, input().split())  # 행, 열
    grid, src_point = [], []
    for i in range(R):
        col = list(map(int, input().split()))
        for j, c in enumerate(col):
            if c:
                src_point.append((i,j))
        grid.append(col)

    # dfs or bfs
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
    def bfs(y: int, x: int):
        q = deque([(y,x)])
        visited[y][x] = 1
        while q:
            weight = 0
            vy, vx = q.popleft()

            # find next 빙산 조각 and 현위치 빙산값 업데이트
            for i in range(4):
                ny, nx = dy[i] + vy, dx[i] + vx
                if -1 < ny < R and -1 < nx < C and not visited[ny][nx]:
                    if not grid[ny][nx]:
                        weight += 1

                    else:
                        q.append((ny, nx))
                        visited[ny][nx] = 1

            grid[vy][vx] -= weight
            if grid[vy][vx] < 0:  # 배열 값은 반드시 0 이상!
                grid[vy][vx] = 0

    def is_valid() -> bool:
        checker = 0
        for i, j in src_point:
            if not grid[i][j]:
                checker += 1
        return len(src_point) == checker

    year = 0
    while True:
        count = 0
        visited = [[0]*C for _ in range(R)]
        for i, j in src_point:
            if grid[i][j] and not visited[i][j]:
                if not count:
                    bfs(i, j)
                    count += 1

                else:
                    print(year)
                    return

        if is_valid():
            print(0)
            return

        year += 1


if __name__ == "__main__":
    solution()
