import sys
from collections import deque


def solution():
    """
    idea: bfs with 1d array
        - 동작 정의:
            - 클립보드 복사 - 화면 붙여넣기
            - 클립보드 복사 - 이모티콘 하나 삭제
            - 그냥 화면에 붙여넣기
            - 그냥 빼기
    """
    # init the data structure
    INF = sys.maxsize
    input = sys.stdin.readline
    N = int(input())
    size = 2*N+1
    grid = [-1]*size

    # do bfs
    q = deque([(1, 0)])  # current length of emoji, length of clip board
    grid[1] = 0
    while q:
        vx, vc = q.popleft()
        vt = grid[vx]
        for i in range(4):
            nx = vx
            nc = vc
            nt = vt
            if not i and nc > 0:  # 현재 클립보드에 있는 이모지를 화면에 붙여 넣기
                nx += nc
                nt += 1

            elif i == 1:  # 화면의 이모지 하나 빼기
                nx -= 1
                nt += 1

            elif i == 2:  # 클립보드에 복사, 화면에서 이모지 하나 빼기
                nc = nx
                nx -= 1
                nt += 2

            elif i == 3:  # 클립보드에 복사, 화면에 붙여넣기
                nc = nx
                nx *= 2
                nt += 2

            if -1 < nx < size and (grid[nx] == -1 or nt < grid[nx]):
                grid[nx] = nt
                q.append((nx, nc))

    print(grid[N])


def solution2():
    """
    idea: bfs with 1d array
        - 큐에 시간도 넣기
        - visited 배열은 그저 방문 기록 용도로만
            - visited 배열을 이중리스트로 만들어야!
            - [화면 이모티콘개수][클립보드 이모티콘 개수]
                - 이렇게 하면, 단순하게 클립보드에 복사하는 연산도, 무한루프를 빠져 나갈 수 있구나
    """
    # init input library
    input = sys.stdin.readline

    # init data structure
    N = int(input())
    size = 2*N+1
    visited = [[0]*size for _ in range(size)]

    # do bfs
    visited[1][0] = 1
    q = deque([(1, 0, 0)])
    while q:
        vx, vc, vt = q.popleft()
        if vx == N:
            print(vt)
            return

        for i in range(3):
            # copy the screen's emoji to clip board
            nx = vx
            nc = vc
            nt = vt + 1
            if not i:
                nx, nc = vx, vx
            # copy the clip board's emoji to screen
            elif i == 1 and vc:
                nx, nc = vx + vc, vc
            # del the one of emoji in screen
            elif i == 2:
                nx, nc = vx-1, vc

            if -1 < nx < size and not visited[nx][nc]:
                visited[nx][nc] = 1
                q.append((nx, nc, nt))


if __name__ == "__main__":
    solution2()
