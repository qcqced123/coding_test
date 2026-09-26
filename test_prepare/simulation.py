def solution1():
    return


def solution2():
    """
    1) check()
        - 현재 칸이 청소가능한가 아닌가
            - 아니면 반시계 방향으로 회전
            - 맞다면 바로 전진
            - 아예 없다면 반드시 원래 방향으로 복귀하고 후진 선택
    """
    N, M = map(int, input().split())
    R, C, D = map(int, input().split())  # starting point
    grid = [list(map(int, input().split())) for _ in range(N)]  # grid

    dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]  # direction vector

    cnt = 0
    while True:
        if grid[R][C] == 0:
            grid[R][C] = 2
            cnt += 1

        moved = False

        for _ in range(4):
            D = (D+3) % 4
            ny = R + dy[D]
            nx = C + dx[D]

            if grid[ny][nx] == 0:
                R = ny
                C = nx
                moved = True
                break

        if moved:
            continue

        back_d = (D+2) % 4
        by = R + dy[back_d]
        bx = C + dx[back_d]

        if grid[by][bx] == 1:
            break

        R = by
        C = bx

    return cnt


def solution3():
    """
    problem:
        - 벽에는 못감
        - 상하좌우
        - 비활성 바이러스 칸에는 갈 수 있음
        - 모든 공간 감염시키는 최소 시간 찾기
        - 0초부터 확산한다는게, 처음 확산한거는 초로 치면 안된다는 소리겠지??

    idea:
    1) 바이러스 리스트 만들기
    2) combination 사용하기
    3) bfs 
    """
    import sys
    import copy
    from collections import deque
    from itertools import combinations

    def bfs(arr, board) -> int:
        cnt = 0
        q = deque()
        q.extend(arr)
        while q:
            for _ in range(len(q)):
                y, x = q.popleft()
                for i in range(4):
                    ny, nx = y + dy[i], x + dx[i]
                    if (
                        -1 < ny < N
                        and -1 < nx < N
                        and board[ny][nx] != 1
                    ):
                        board[ny][nx] = 2
                        q.append((ny,nx))

            cnt += 1

        # check state of grid
        state = True
        for i in range(N):
            for j in range(N):
                if board[i][j] == 0:
                    state = False

        return cnt if state else sys.maxsize

    # input
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]  # grid

    # direction array
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

    # make virus list
    virus_list = [
        (i,j)
        for i in range(N)
        for j in range(N)  
        if grid[i][j] == 2
    ]

    # bfs
    answer = sys.maxsize
    for comb in combinations(virus_list, M):
        board = copy.deepcopy(grid)
        answer = min(answer, bfs(comb, board))

    return -1 if answer == sys.maxsize else answer


def solution3_review():
    import sys
    from collections import deque
    from itertools import combinations

    def bfs(arr):
        q = deque()
        dist = [[-1]*N for _ in range(N)]

        for y,x in arr:
            q.append([y,x])
            dist[y][x] = 0

        infected = 0
        max_time = 0
        while q:
            y, x = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if not(-1 < ny < N and -1 < nx < N):
                    continue

                if grid[ny][nx] == 1 or dist[ny][nx] != -1:
                    continue

                dist[ny][nx] = dist[y][x] + 1
                q.append([ny,nx])

                if grid[ny][nx] == 0:
                    infected += 1
                    max_time = dist[ny][nx]

        return max_time if infected == empty_count else sys.maxsize


    # input
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]  # grid

    # direction array
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

    # make virus list
    virus_list = [
        (i,j)
        for i in range(N)
        for j in range(N)  
        if grid[i][j] == 2
    ]

    empty_count = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0:
                empty_count += 1

    # bfs
    answer = sys.maxsize
    for comb in combinations(virus_list, M):
        answer = min(answer, bfs(comb))

    return -1 if answer == sys.maxsize else answer

if __name__ == "__main__":
    print(solution3_review())