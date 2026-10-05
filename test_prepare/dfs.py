"""
DFS:
최단거리 측정보다는,
1) 연결된 영역 개수
2) 섬의 개수
3) 같은 그룹 찾기
4) 특정 위치에서 갈 수 있는 모든 칸 찾기


DFS vs BFS:
1) 연결 여부, 영역이 몇개인가, 그룹의 크기, 상태를 끝까지 추적해야 하는 경우
2) 최소 거리, 최소 이동 횟수, 몇 초 뒤 도착, 가장 가까운 대상, 최단거리

=> 둘을 구분하는 핵심은 최단거리가 필요한가 여부. 최단거리가 필요하면 무조건 bfs로 접근
=> 나머지 문제는 그냥 취향 차이
"""
def solution1():
    """
    problem
    1) 섬의 개수
    2) 가장 큰 섬의 크기 측정

    idea:
        1) dfs + visited 
    """
    import sys
    sys.setrecursionlimit(10**6)

    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    visited = [[-1]*M for _ in range(N)]

    dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

    # dfs interface func
    def dfs(y, x):
        """
        return:
            current size of found island
        """
        size = 1
        visited[y][x] = 1
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if (
                -1 < ny < N
                and -1 < nx < M
                and grid[ny][nx] == 1
                and visited[ny][nx] == -1
            ):
                size += dfs(ny, nx)
                
        return size

    # for-loop for find new island
    cnt = 0
    max_size = 0
    for i in range(N):
        for j in range(M):
            if (
                grid[i][j] == 1
                and visited[i][j] == -1
            ):
                max_size = max(max_size, dfs(i, j))
                cnt += 1
        
    return cnt, max_size


def solution1_review():
    """섬의 개수와 가장 큰 섬의 크기를 계산한다.
    iterative stack implementation version
    """
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    def dfs(sy, sx):
        """시작점과 연결된 섬의 크기를 반환한다."""
        stack = [(sy, sx)]
        visited[sy][sx] = True

        size = 0

        while stack:
            y, x = stack.pop()
            size += 1

            for d in range(4):
                ny = y + dy[d]
                nx = x + dx[d]

                if (
                    0 <= ny < N
                    and 0 <= nx < M
                    and grid[ny][nx] == 1
                    and not visited[ny][nx]
                ):
                    visited[ny][nx] = True
                    stack.append((ny, nx))

        return size

    count = 0
    max_size = 0

    for y in range(N):
        for x in range(M):
            if grid[y][x] == 1 and not visited[y][x]:
                size = dfs(y, x)
                count += 1
                max_size = max(max_size, size)

    return count, max_size


def solution2():
    """
    problem:
        1) 카메라 번호에 따라서 감시 방향이 달라짐
        2) 카메라 방향 선택에 따라서 빈 공간 최소 개수를 백트래킹으로 구해야 할 듯
            - 즉 카메라 별로 탐색 가능한 방향도 선택을 해줘야 하는거지 지금
        
    idea:
        
    implementation:
        - camera list
        - camera direction dictionary
        - dfs interface
    """
    import sys
    from copy import deepcopy

    sys.setrecursionlimit(10**6)
    N, M = map(int, input().split())  # grid size, number of cameras
    grid = [list(map(int, input().split())) for _ in range(N)]   # grid

    # direction vector, dictionary
    dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

    camera_direction = {
        1: [[0],[1],[2],[3]],
        2: [[0,2], [1,3]],
        3: [[0,1], [1,2], [2,3], [3,0]],
        4: [[0,1,2], [1,2,3], [0,2,3], [0,1,3]],
        5: [[0,1,2,3]],
    }

    # 1) find the cameras
    cameras = [
        (i,j,grid[i][j])
        for i in range(N)
        for j in range(M)
        if 0 < grid[i][j] < 6
    ]
    nums = len(cameras)

    # 2) backtrack interface func
    answer = sys.maxsize
    def dfs(camera_index: int, board: list[list[int]]):
        nonlocal answer

        # end condition of dfs
        if camera_index == nums:
            cnt = 0
            for i in range(N):
                for j in range(M):
                    if board[i][j] == 0:
                        cnt += 1

            answer = min(answer, cnt)

            return None

        # get data from dictionary, list
        y, x, t = cameras[camera_index]
        candidates = camera_direction[t]

        # back tracking
        for candidate in candidates:
            current_board = deepcopy(board)

            # 감시 처리
            for d in candidate:
                ny, nx = y + dy[d], x + dx[d]

                while -1 < ny < N and -1 < nx < M:
                    if current_board[ny][nx] == 6:
                        break

                    if current_board[ny][nx] == 0:
                        current_board[ny][nx] = -1

                    ny += dy[d]
                    nx += dx[d]

            dfs(camera_index+1, current_board)

        return None
    
    dfs(0, grid)

    return answer


def solution3():
    """
    idea: back tracking
        1) 스택별 상태 관리
        2) 종료조건
        3) 되돌리기 로직
            - 재귀에서 돌아왔을 때 내가 탐색하면서 만든 상태를 원래대로 되돌려 줘야 함
            - 그게 귀찮으면 그냥 deepcopy써서 스택별로 상태 기록지를 따로 격리해버리던가
        4) 무엇을 탐색시킬 것인가
        5) pruning logic 도 최적화에 필요할 수도
            - 예를 들어 이번 문제에서 이미 현재 탐색한 원소값들이 이미 K 를 넘겼으면 해당 path는 더이상 탐색할 이유가 없음
    """
    import sys

    # input
    sys.setrecursionlimit(10**6)
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))

    # back tracking interface
    answer = -1
    def dfs(nums: list[int], cache: list[int]):
        # end condition
        nonlocal answer
        if len(cache) == M:
            cnt = sum(cache)
            if cnt <= K:
                answer = max(answer, cnt)

            return None

        # back tracking logic
        for i,num in enumerate(nums):
            cache.append(num)
            dfs(
                nums=nums[i+1:],
                cache=cache
            )
            cache.pop()

        return

    dfs(nums=arr, cache=[])

    return answer


def solution4():
    """ 바이러스 격리벽
    problem: 

    idea: back track + bfs
    """
    from copy import deepcopy
    from collections import deque
    from itertools import combinations

    # bfs func
    def bfs(arr: list[tuple[int]], current_board: list[list[int]]) -> int:
        q = deque()
        dist = [[-1]*M for _ in range(N)]

        for position in arr:
            y, x = position
            dist[y][x] = 1
            q.append(position)
            
        while q:
            y, x = q.popleft()

            for d in range(4):
                ny, nx = y + dy[d], x + dx[d]

                if (
                    -1 < ny < N 
                    and -1 < nx < M
                    and current_board[ny][nx] != 1
                    and dist[ny][nx] == -1
                ):
                    dist[ny][nx] = 1
                    current_board[ny][nx] = 2
                    q.append((ny,nx))                

        # finally count last zero value in board
        cnt = 0
        for i in range(N):
            for j in range(M):
                if current_board[i][j] == 0:
                    cnt += 1

        return cnt

    # get input
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # make candidates of new wall
    candidates = [
        (i,j)
        for i in range(N)
        for j in range(M)
        if grid[i][j] == 0 
    ]

    virus_list = [
        (i,j)
        for i in range(N)
        for j in range(M)
        if grid[i][j] == 2
    ]

    # direction vector
    dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

    # back tracking interface
    answer = -1 
    for candidate in combinations(candidates, 3):
        # record current state
        board = deepcopy(grid)
        for position in candidate:
            y, x = position
            board[y][x] = 1
            
        # bfs interface
        result = bfs(
            arr=virus_list,
            current_board=board
        )
        answer = max(answer, result)
    return answer


def solution5():
    """ Day 11 아침, 방향성 스프링클러 (백트래킹에서 상태를 복사하지 않고 원복 시키기)
    apply() -> dfs() -> undo()

    1) 겹칠 수 있는 상태에 대해서는 카운트 배열을 쓰기
    2) 행동을 함수로 정확히 추상화해서 분리해야 함
    """
    import sys

    sys.setrecursionlimit(10**6)

    # get input
    N, M = map(int, input().split())
    board = [list(input().strip()) for _ in range(N)]

    # make sprinklr list
    sprinklrs = [
        (i,j)
        for i in range(N)
        for j in range(M)
        if board[i][j] == "S"
    ]

    # utils
    def apply(d, idx, dist, mode):
        y,x = sprinklrs[idx]

        ny = y
        nx = x

        if d == "H":
            
            # record left side
            while True:
                nx -= 1

                if not (-1 < nx < M and board[ny][nx] != "#"):
                    break

                dist[ny][nx] += mode
                

            # record right side
            while True:
                nx += 1

                if not (-1 < nx < M and board[ny][nx] != "#"):
                    break

                dist[ny][nx] += mode

        if d == "V":
            # record upper side
            while True:
                ny -= 1

                if not (-1 < ny < N and board[ny][nx] != "#"):
                    break

                dist[ny][nx] += mode
                

            # record down side
            while True:
                ny += 1
                nx = x

                if not (-1 < ny < N and board[ny][nx] != "#"):
                    break

                dist[ny][nx] += mode

        return

    def evaluate():
        result = 0 
        for i in range(N):
            for j in range(M):
                if board[i][j] == "." and dist[i][j] == 0:
                    result += 1 
        return result

    # dfs func
    answer = sys.maxsize
    dist = [[0]*M for _ in range(N)]
    def dfs(idx, dist):
        nonlocal answer
        # end condition
        if idx == len(sprinklrs):
            answer = min(
                answer,
                evaluate()
            )
            return

        # set direction and call next stack
        for d in ["H", "V"]:
            apply(
                d,
                idx,
                dist,
                1
            )
            dfs(idx+1, dist)
            apply(
                d,
                idx,
                dist,
                -1
            )

        return

    dfs(0, dist)

    return answer


def solution6():
    """ 순환 정비 벨트 (Day 11 저녁)
    """

    return


if __name__ == "__main__":
    print(solution5())