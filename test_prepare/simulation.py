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


def solution4():
    """ 오염 확산, (Day 7 오전 문제)
    point: 읽는 상태, 쓰는 상태 분리가 필요함, 
    이럴 때는 bfs 쓰던가 이번 코드처럼 그냥 deepcopy 비슷한 방식으로 복사하되, 읽는 상태와 쓰는 상태를 분리하면 된다.
    
    idea: simulation
    """
    # get input
    N, M, T = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # direction vector
    dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

    # simulation, bfs interface
    for _ in range(T):
        next_grid = [row[:] for row in grid]

        for y in range(N):
            for x in range(M):
                # if not virus value
                if grid[y][x] != 1:
                    continue

                for d in range(4):
                    ny, nx = y + dy[d], x + dx[d]

                    if not (-1 < ny < N and -1 < nx < M):
                        continue

                    if grid[ny][nx] != 0:
                        continue

                    next_grid[ny][nx] = 1

        grid = next_grid
    
    # calculate answer
    answer = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                answer += 1

    return answer


def solution5():
    """ 에너지 구체 융합 실험 (Day 7 저녁)

    problem:

    state:
        - 변하는 것:
            - 그리드
            - 구체 상태 정보
        - 고정: 

    implementation:
        - 보드가 필요할까: 여기에 구체 정보를 담아 줘야해서 필요할 듯
        - 구체들 정보 담을 자료구조는 뭐가 가장 편할까: 그냥 그리드에 담아 놓는게 나을듯, 너무 변동이 많아서 들고 다니기 힘들어
        - 매번 실행마다 수행할 동작 정의:
            - 구체 이동(동시 처리)
                - 그리드 넘어가는거 방향 처리해주는게 너무 어려운데... 이거 어케 구현하지... 이게 병목이네 오히려...
                - 양의 방향: (위치 + 속도) % N
                - 음의 방향: (N + (위치 - 속도)) % N

            - 합쳐지고, 사라질 구체 찾아서 계산하기
                - 질량, 속도, 방향 판정
                - 새로운 질량이 0이면 소멸
                - 아니면 새롭게 정해진 네가지 방향으로 퍼뜨림 (다음 턴에 움직이게 하면 된다)
    """
    import sys

    # util func
    def print_board(grid):
        for i in range(N):
            print(grid[i], end="\n")

        return None

    def cal_positive(i, s):
        return i % N

    def cal_negative(i, s):
        return (N + i) % N


    # get input
    N, M, K = map(int, input().split())
    board = [[(0,0,0,0)]*N for _ in range(N)] 


    # initialize board
    for _ in range(M):
        y,x,m,s,d = map(int, input().split())
        board[y-1][x-1] = (m,s,d,1)  # 질량, 속도, 방향, 개수


    # direction vector
    dy, dx = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]


    # simulation interface
    for _ in range(K):
        current_board = [row[:] for row in board]

        # 보드에 남아 있는 구체들 움직이기
        for y in range(N):
            for x in range(N):
                m,s,d,c = board[y][x]

                if c == 0:
                    continue

                # 스피드 초기화
                s %= N

                # 기존 칸 초기화
                current_board[y][x] = (0,0,0,0)

                # 일반 적인 경우의 무빙 처리
                if c == 1:
                    ny, nx = y + s*dy[d], x + s*dx[d]

                    # 그리드 벗어나는 경우 처리
                    if not (-1 < ny < N and -1 < nx < N):
                        if ny > N-1:
                            ny = cal_positive(ny, s)

                        if ny < 0:
                            ny = cal_negative(ny, s)

                        if nx > N-1:
                            nx = cal_positive(nx, s)

                        if nx < 0:
                            nx = cal_negative(nx, s)
                    
                    # 이동 처리
                    current_board[ny][nx] = (
                        current_board[ny][nx][0] + m,
                        current_board[ny][nx][1] + s,
                        current_board[ny][nx][2] + d,
                        current_board[ny][nx][3] + 1,
                    )


                # 합쳐졌던 칸 무빙 처리
                if c == 4:
                    # 짝수
                    if d % 2 == 0:
                        for d in [0,2,4,6]:
                            ny, nx = y + s*dy[d], x + s*dx[d]

                            # 그리드 벗어나는 경우 처리
                            if not (-1 < ny < N and -1 < nx < N):
                                if ny > 0:
                                    ny = cal_positive(ny, s)
        
                                if ny < 0:
                                    ny = cal_negative(ny, s)
        
                                if nx > 0:
                                    nx = cal_positive(nx, s)
        
                                if nx < 0:
                                    nx = cal_negative(nx, s)
        
                            # 이동 처리
                            current_board[ny][nx] = (
                                current_board[ny][nx][0] + m,
                                current_board[ny][nx][1] + s,
                                current_board[ny][nx][2] + d,
                                current_board[ny][nx][3] + 1,
                            )
                    # 홀수
                    if d % 2 == 1:  
                        for d in [1,3,5,7]:
                            ny, nx = y + s*dy[d], x + s*dx[d]

                            # 그리드 벗어나는 경우 처리
                            if not (-1 < ny < N and -1 < nx < N):
                                if ny > 0:
                                    ny = cal_positive(ny, s)
        
                                if ny < 0:
                                    ny = cal_negative(ny, s)
        
                                if nx > 0:
                                    nx = cal_positive(nx, s)
        
                                if nx < 0:
                                    nx = cal_negative(nx, s)
        
                            # 이동 처리
                            current_board[ny][nx] = (
                                current_board[ny][nx][0] + m,
                                current_board[ny][nx][1] + s,
                                current_board[ny][nx][2] + d,
                                current_board[ny][nx][3] + 1,
                            )

        # 합치고 쪼갤거, 소멸시킬거 처리해주기
        for y in range(N):
            for x in range(N):
                m,s,d,c = current_board[y][x]

                # 구체 한 개이거나, 없는 칸 넘어가기
                if c <= 1:
                    continue

                # 합치기
                # d는 냅둬도 상관 없음
                new_m = m // 5
                new_s = s // c
                new_d = d

                # 질량 없는 경우 날리기
                if new_m == 0:
                    current_board[y][x] = (0,0,0,0)
                    continue

                # 쪼개기
                current_board[y][x] = (
                    new_m,
                    new_s,
                    new_d,
                    4
                )

        # 보드 교체
        board = current_board


    # calculate
    answer = 0
    for y in range(N):
        for x in range(N):
            m,s,d,c = board[y][x]

            if c >= 1:
                answer += m*c

    return answer


def solution5_retry():
    """
    목적: 
        - 상태 공간 정의를 새롭게 다시 하기 위해
        - 기존 방법으로는 합칠 때 방향 결정을 제대로 못해줌
        - 한 공간에 4개의 구체가 모였는데, 만약 홀홀짝짝이라면 합은 또 짝수라서 기존 내 풀이로는 구분을 제대로 못함
    

    """
    # get input
    N, M, K = map(int, input().split())
    board = [[[] for _ in range(N)] for _ in range(N)]


    # initialize board
    for _ in range(M):
        y,x,m,s,d = map(int, input().split())
        board[y-1][x-1].append((m,s,d))  # 질량, 속도, 방향


    # direction vector
    dy, dx = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

    # simulation interface
    for _ in range(K):
        current_board = [[[] for _ in range(N)] for _ in range(N)]  # 읽기와 쓰기를 분리하기 위해서 아예 텅빈 자료구조를가져옴

        # 보드에 남아 있는 구체들 움직이기
        for y in range(N):
            for x in range(N):
                current_position = board[y][x]

                if not current_position:
                    continue

                # 무빙 처리
                for ball in current_position:
                    m,s,d = ball
                    ny, nx = (y + s*dy[d]) % N, (x + s*dx[d]) % N  # 이렇게 해야 내 수식대로 계산 할 수 있음
                    
                    # 이동 처리
                    current_board[ny][nx].append((m,s,d))

        # 합치고 쪼갤거, 소멸시킬거 처리해주기
        for y in range(N):
            for x in range(N):
                current_position = current_board[y][x]
                # 구체 한 개이거나, 없는 칸 넘어가기
                if len(current_position) <= 1:
                    continue

                # 합치기
                new_m = 0
                new_s = 0
                new_d = {"짝수": 0, "홀수": 0}  # 0
                for ball in current_position:
                    m,s,d = ball
                    new_m += m
                    new_s += s

                    if d % 2 == 0:
                        new_d["짝수"] += 1

                    if d % 2 == 1:
                        new_d["홀수"] += 1
                
                # 합치기
                # d는 냅둬도 상관 없음
                new_m //= 5

                # 질량 없는 경우 날리기
                if new_m == 0:
                    current_board[y][x] = []
                    continue

                new_s //= len(current_position)
                new_d = [1,3,5,7] if (new_d["짝수"] > 0 and new_d["홀수"] > 0) else [0,2,4,6]

                # 쪼개기
                current_board[y][x] = [
                    (new_m, new_s, new_d[d])
                    for d in range(4)
                ]

        # 보드 교체
        board = current_board

    # 정답 계산
    answer = 0
    for y in range(N):
        for x in range(N):
            ball = board[y][x]
            if not ball:
                continue

            for state in ball:
                m,s,d = state
                answer += m

    return answer


def solution6_sub():
    """ 하위 서브 구현 문제 (Day8 저녁)
    """

    from collections import deque

    # direction vector
    dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

    N = 5

    body = deque([
        (2, 1),
        (2, 2),
    ])

    occupied = {
        (2, 1),
        (2, 2),
    }

    batteries = {
        (2, 3),
        (4, 4),
    }

    d = 0

    # define board 
    board = [[-1]*N for _  in range(N)]
    for battery in batteries:
        y,x = battery
        board[y][x] = 1

    def move_once(body, occupied, batteries, d, N):
        """
        로봇을 현재 방향으로 정확히 한 칸 이동시킨다.
        state:
            - 머리 방향: 방향 벡터값 확인 해서 결정

        return:
            alive: 충돌하지 않았는지 (머리와 몸이 충돌하거나, 머리가 격자 밖이거나)
            ate: 배터리를 먹었는지
        """
        alive = True
        ate = False

        # determine which element is head
        
        y, x = body[-1]
        ny, nx = y + dy[d], x + dx[d]
        if not (-1 < ny < N and -1 < nx < N) or ((ny, nx) in occupied):
            alive = False
            ate = False
            return (alive, ate)

        body.append((ny,nx))
        occupied.add((ny,nx))

        if (ny, nx) in batteries:
            ate = True
            batteries.remove((ny,nx))  # pop()은 무작위 원소를 빼는거고, remove를 해야 키값 기반으로 빼준다

        else:
            y, x= body.popleft()
            occupied.remove((y,x))
        
        return (alive, ate)

    return


def solution6():
    """ 꼬리형 점검 로봇 (Day8 저녁)
    state:
        - batteries: set, 남은 배터리
        - occupied: set, 몸통이 차지하는 공간, 상수 시간 내에 검색하기 위해서 set로 사용
        - body: deque, 머리, 가장 마지막 꼬리 위치 파악하기 위함
        - commands: deque, 방향 회전 명령어 담긴 리스트
        - ate: 배터리를 먹었나 안먹었나 상태 표시
        - alive: 머리 혹은 격자 바깥이랑 충돌했나 상태 표시
        - direction: 현재 머리 방향

    workflow:
        - 현재 방향으로 머리 이동 (초기값 오른쪽)
        

    return: 
        충돌해서 종료되는 시간초
    """
    from collections import deque

    # get input
    N = int(input())
    K = int(input())

    batteries = set()
    for _ in range(K):
        y, x = tuple(map(int, input().split()))
        batteries.add((y-1, x-1))

    L = int(input())
    commands = deque()
    for _ in range(L):
        commands.append(tuple(input().split()))
    
    body = deque()
    body.append((0,0))

    occupied = {(0,0)}

    # direction vector
    dy, dx = [-1, 0, 1, 0], [ 0, 1, 0, -1]


    # define state
    time = 0
    direction = 1

    while True:
        time += 1

        # 머리 이동 시키기
        y, x = body[-1]
        ny, nx = y + dy[direction], x + dx[direction]
        if not (-1 < ny < N and -1 < nx < N) or (ny,nx) in occupied:  # 충돌 처리: 머리통이 격자밖이거나 몸통이랑 겹치거나
             break

        body.append((ny,nx))
        occupied.add((ny,nx))

        # 배터리 먹은 경우/못 먹은 경우 처리
        if not (ny,nx) in batteries:  # 배터리 못 먹은 경우
            ry, rx = body.popleft()
            occupied.remove((ry, rx))

        # 배터리 먹은 경우 먹은 처리 해주기
        if (ny, nx) in batteries:
            batteries.remove((ny,nx))

        # 방향 전환 처리
        if commands and int(commands[0][0]) == time:
            _, command = commands.popleft()
            if command == "L":
                direction = (direction - 1) % 4
            else:  # D
                direction = (direction + 1) % 4
        

    return time



if __name__ == "__main__":
    print(solution5_retry())





