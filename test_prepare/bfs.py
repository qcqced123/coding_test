"""
bfs

1)
"""
def solution1():
    """ 긴급통로, Day 6 아침 문제
    problem:
        - 상하좌우 이동 가능, 한 칸씩
        - 벽을 한 번 뚫을 수 있음 (이것도 이동 횟수에 포함되어야 함)

    idea: 3D bfs

    """
    from collections import deque

    # bfs func
    def bfs(y,x):
        q = deque()
        q.append((y,x,0))
        dist = [[[-1]*2 for _ in range(M)] for _ in range(N)]

        dist[y][x][0] = 0

        """
        y,x: 좌표
        s: state, 벽을 뚫었나 안뚫었나
        """
        while q:
            y,x,s = q.popleft()

            for d in range(4):
                ny, nx = y + dy[d], x + dx[d]

                if not (-1 < ny < N and -1 < nx < M):
                    continue

                if grid[ny][nx] == 0:
                    if dist[ny][nx][s] == -1:  # not visited
                        q.append((ny,nx,s))
                        dist[ny][nx][s] = dist[y][x][s] + 1
                        
                else:
                    if (s == 0 and dist[ny][nx][1] == -1):
                        q.append((ny,nx,1))
                        dist[ny][nx][1] = dist[y][x][s] + 1

        # get answer from bfs result
        candidate_1 = dist[N-1][M-1][0]
        candidate_2 = dist[N-1][M-1][1]

        if candidate_1 == -1:
            return candidate_2

        if candidate_2 == -1:
            return candidate_1

        return min(candidate_1, candidate_2)
    
    # get input
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # direction vector
    dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

    # bfs interface
    answer = bfs(0,0)

    return answer


def solution2():
    """ 회수로봇, Day 6 저녁
    problem:

    idea: bfs

    implementation:
        - 로봇 시작 위치 찾기 (0)
        - 폐기물 위치 리스트 만들기 (0)
        - 거리 측정 모듈 만들기
        - bfs 구현 (시간 측정해야 해서 필요함)

    """
    import sys
    from collections import deque

    # bfs func
    def bfs(y: int, x: int, target_y: int, target_x: int):
        """
        Args:
            y: 로봇의 시작 위치 y 좌표
            x: 로봇의 시작 위치 x 좌표
            target_y: 현재 거리 측정 대상 y 좌표
            target_x: 현재 거리 측정 대상 x 좌표
        """
        q = deque()
        q.append((y,x))  # y, x
        dist = [[-1]*N for _ in range(N)]  # 거리측정
        dist[y][x] = 0
        
        while q:
            py, px = q.popleft()
            for d in range(4):
                ny, nx = py + dy[d], px + dx[d]
                if not (-1 < ny < N and -1 < nx < N):
                    continue

                if robot_level < grid[ny][nx] or dist[ny][nx] != -1:
                    continue

                q.append((ny,nx))
                dist[ny][nx] = dist[py][px] + 1

                if (ny == target_y and nx == target_x):
                    return dist[ny][nx]

        return sys.maxsize

    # get input
    N = int(input())
    grid = [list((map(int, input().split()))) for _ in range(N)]

    # direction vector
    dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

    # get trash list, starting point index
    trashes = []
    robot_y, robot_x = None, None
    for y in range(N):
        for x in range(N):
            if grid[y][x] == 9:
                robot_y, robot_x = y, x
                grid[robot_y][robot_x] = 0

            if 1 <= grid[y][x] <= 6:
                trash_level = grid[y][x]
                trashes.append((y,x,trash_level))

    # define robot state
    time = 0
    eaten = 0
    robot_level = 2
    loop_state = True

    # bfs interface
    while loop_state:
        state_list = []
        for trash in trashes:
            ty, tx, tl = trash

            # 로봇 레벨보다 쓰레기 레벨이 높거나 같은 경우, 현재 회수 불가능하기 때문에 넘김
            if robot_level <= tl:
                continue

            # 거리 측정
            cnt = bfs(robot_y, robot_x, ty, tx)

            # 상태 사전에 기록
            state_list.append((cnt, ty, tx, tl))

        # 로봇 상태 업데이트
        state_list.sort(key=lambda x: (x[0], x[1], x[2]))

        if not state_list:
            break
        
        distance, trash_y, trash_x, _ = state_list[0]
        if distance == sys.maxsize:
            break

        eaten += 1
        time += distance
        robot_y = trash_y
        robot_x = trash_x
        grid[robot_y][robot_x] = 0

        if eaten == robot_level:
            eaten = 0
            robot_level += 1

        for i, trash in enumerate(trashes):
            if (trash_y == trash[0] and trash_x == trash[1]):
                trashes.pop(i)
    
    return time


def solution2_refactoring():
    import sys
    from collections import deque

    # bfs func
    def bfs(y: int, x: int):
        """
        point:
            - bfs는 한번만 돌리기
            - 튜플 특성 이용해서 코드 짜기 (튜플은 사전식으로 비교하기 때문에 원소의 인덱스 순서별로 원소값을 비교함)
            - 정렬도 굳이 필요 없음

        Args:
            y: 로봇의 시작 위치 y 좌표
            x: 로봇의 시작 위치 x 좌표
        """
        q = deque()
        q.append((y,x))  # y, x
        dist = [[-1]*N for _ in range(N)]  # 거리측정
        dist[y][x] = 0
        
        while q:
            py, px = q.popleft()
            for d in range(4):
                ny, nx = py + dy[d], px + dx[d]
                if not (-1 < ny < N and -1 < nx < N):
                    continue

                if robot_level < grid[ny][nx] or dist[ny][nx] != -1:
                    continue

                q.append((ny,nx))
                dist[ny][nx] = dist[py][px] + 1

        return dist

    # get input
    N = int(input())
    grid = [list((map(int, input().split()))) for _ in range(N)]

    # direction vector
    dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

    # get trash list, starting point index
    trashes = []
    robot_y, robot_x = None, None
    for y in range(N):
        for x in range(N):
            if grid[y][x] == 9:
                robot_y, robot_x = y, x
                grid[robot_y][robot_x] = 0

            if 1 <= grid[y][x] <= 6:
                trash_level = grid[y][x]
                trashes.append((y,x,trash_level))

    # define robot state
    time = 0
    eaten = 0
    robot_level = 2

    # bfs interface
    while True:
        candidates = []
        dist = bfs(robot_y, robot_x)
    
        for ty, tx, tl in trashes:
            if tl < robot_level and dist[ty][tx] != -1:
                candidates.append((dist[ty][tx], ty, tx, tl))

        
        # 로봇 상태 업데이트
        if not candidates:
            break

        # 튜플은 원래 사전식으로 맨 앞ㅍ에 원소부터 차례대로 비교함
        distance, trash_y, trash_x, trash_level = min(candidates)
        if distance == sys.maxsize:
            break

        eaten += 1
        time += distance
        robot_y = trash_y
        robot_x = trash_x
        grid[robot_y][robot_x] = 0

        trashes.remove((trash_y, trash_x, trash_level))

        if eaten == robot_level:
            eaten = 0
            robot_level += 1
    
    return time


if __name__ == "__main__":
    print(solution2_refactoring())