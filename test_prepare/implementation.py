def solution1():
    """
    problem: 사각형 회전시키기, (Day 9 아침 구현)
    """
    def rotate_square(board, r, c, L):
        """
        board의 (r,c)를 좌상단으로 하는
        L×L 영역을 시계 방향 90도 회전한다.

        1) 사각형 범위 확정
            - 끝자리 좌표 확정
            - 기록할 보드 초기화

        2) 회전 구현
        """
        # 사각형 범위 확정
        # 인덱스 값
        end_r = r + L - 1
        end_c = c + L - 1

        # 변수 상태값/정답 그리드 정의
        row_size = len(board)
        col_size = len(board[0])
        answer = [
            row[:]
            for row in board
        ]

        # 회전 시작
        for l in range(L, 1, -2):
            # 상단 탐색
            for i in range(l-1):
                answer[r+i][end_c] = board[r][c+i]

            # 오른쪽 탐색
            for i in range(l-1):
                answer[end_r][end_c-i] = board[r+i][end_c]

            # 하단 탐색
            for i in range(l-1):
                answer[end_r-i][c] = board[end_r][end_c-i]

            # 왼쪽 탐색
            for i in range(l-1):
                answer[r][c+i] = board[end_r-i][c]
            
            # update state
            r += 1
            c += 1
            end_r -= 1
            end_c -= 1

        return answer

    
    def rotate_square_answer(board, r, c, L):
        """(r, c)를 좌상단으로 하는 L×L 영역을 시계방향 90도 회전한다."""
        answer = [row[:] for row in board]

        for i in range(L):
            for j in range(L):
                answer[r + j][c + L - 1 - i] = board[r + i][c + j]

        return answer


    # get input
    board = [
        [1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]
    ]

    answer = rotate_square(
        board=board,
        r=1,
        c=1,
        L=3
    )

    # print answer
    for i in range(len(board)):
        print(answer[i], end="\n")

    return answer


def solution2():
    """
    1) 구름 이동 시키기 (순환 격자)
    2) 구름 위치에 물 양 1 증가
    3) 대각선 물 복사
        - 물 양이 1이상인 대각선 칸에 1씩 증가
        - 순환 이동 무시 여기서는
    4) 구름 모두 제거
    5) 물 양이 2인 칸이면서 이번 명령에서 구름이 없었던 칸에 구름 생성
    6) 구름이 생긴 칸은 물 양 2 감소

    Return:
        M 개 명령 수행 후 남은 물의 총량

    Note:
        단계를 임의로 합치니까 틀리게 되는구나, 분리하자
    """
    # get input
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    commands = [list(map(int, input().split())) for _ in range(M)]

    # direction vector
    dy, dx = [0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]

    # make cloud set
    clouds = {
        (N-1,0),
        (N-1,1),
        (N-2,0),
        (N-2,1),
    }

    def move_clouds(clouds, d, s, N):
        """
        순환 격자에서 모든 구름을 d 방향으로 s칸 이동시킨 뒤
        새로운 좌표 집합을 반환한다.

        Return: new cloud set
        """
        result = set()
        for cloud in clouds:
            cy, cx = cloud

            # get new position
            ny, nx = (cy + s*dy[d-1]) % N, (cx + s*dx[d-1]) % N
            result.add((ny,nx))
        
        return result

    # simulation interface
    for command in commands:
        cd, cs = command
        clouds = move_clouds(
            clouds=clouds,
            d=cd,
            s=cs,
            N=N
        )
        # 2) 구름 위치에 물 양 1 증가
        for cloud in clouds:
            cy, cx = cloud
            board[cy][cx] += 1

        # 3) 대각선 물복사
        for cloud in clouds:
            cache = 0
            cy, cx = cloud
            for i in [1, 3, 5, 7]:
                ny, nx = cy + dy[i], cx + dx[i]
                if not (-1 < ny < N and -1 < nx < N):
                    continue

                if (board[ny][nx] > 0):
                    cache += 1

            board[cy][cx] += cache
            

        # 3) 구름 생성 / 물 양 감소 시키기
        new_clouds = set()
        for y in range(N):
            for x in range(N):
                if board[y][x] >= 2 and not (y,x) in clouds: # 이거 마지막 구름 위치만 추적해두면 되는건가
                    new_clouds.add((y,x))
                    board[y][x] -= 2
        
        clouds = new_clouds

    # 4) 정답 계산
    answer = 0
    for i in range(N):
        for j in range(N):
            answer += board[i][j]

    return answer


def solution3():
    """ Day 12 아침 구현 과제
    """
    from collections import defaultdict
    board = [
        ".....",
        ".#...",
        ".....",
        "...#.",
        ".....",
    ]

    agents = [
        (3, 0, 0, 1),
        (1, 0, 2, 3),
        (2, 1, 0, 1),
        (4, 4, 4, 2),
    ]

    dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

    def move_agents(board, agents):
        """
        모든 로봇을 동시에 한 번 이동시킨 뒤
        충돌을 처리하고 살아남은 로봇 목록을
        id 오름차순으로 반환한다.
        """
        N = len(board)
        M = len(board[0])
        new_position = defaultdict(list)
        for agent in agents:
            a_id, a_y, a_x, a_d = agent

            ny, nx = a_y + dy[a_d], a_x + dx[a_d]
            if not (-1 < ny < N and -1 < nx < M and board[ny][nx] != "#"):
                ny = a_y
                nx = a_x    

            # add new_position
            new_position[(ny,nx)].append((a_id, ny, nx, a_d))

        result = [min(position) for position in new_position.values()]
        result.sort()

        return result

    new_agents = move_agents(
        board=board,
        agents=agents
    )
    return new_agents


def solution4():
    """
    """
    return



if __name__ == "__main__":
    print(solution3())
