from collections import deque


def solution(board):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/67259

    summary:
        1) 경주로 건설
          - 정사각형 격자
          - 시작 to 도착
          - 상하좌우 인접 칸 중에서 2개 칸 선택 가능
            - 직선도로: 100원
            - 코너도로: 500원
    return:
        1) 최소 비용으로 도로 연결

    solution:
        1) 2D Table with BFS
          - 이전 도로의 상태를 알아야 할 듯
            - 이전과 수평이 아니라면, 추가 비용 400원 이렇게
            - 큐에 이전 방향을 넣어주면 되겠구만
            - 코너 자체가 돈이 되는구나
          - visit 배열에 있어도 최소값이거나
          - visit 배열에 없거나

    => 2차원 테이블로 풀면 아래와 같은 반례를 해결 못함, 이전 경로의 방향까지 고려해야 반례가 없어진다
    => 따라서 방향까지 고려하는 3차원 테이블이 필요하다.
    => 고려할게 많으면 그냥 테이블 차원을 추가하도록 하자, 그게 제일 확실하다
    inputs:
        [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [1, 1, 1, 0, 0]]

    2D Table return:
        3300

    3D Table return:
        3000
    """
    N = len(board)
    dy, dx = (-1, 0, 1, 0), (0, -1, 0, 1)
    visit = [[[0, 0, 0, 0] for _ in range(N)] for _ in range(N)]

    def is_valid(curr_y: int, curr_x: int):
        return -1 < curr_y < N and -1 < curr_x < N and board[curr_y][curr_x] != 1

    def cost_cal(past_d: int, curr_d: int, past_c: int) -> int:
        cost = 100 if past_d % 2 == curr_d % 2 else 600
        total = past_c + cost
        return total

    def bfs(y: int, x: int):
        q = deque([(None, 0, y, x)])
        for i in range(4):
            visit[y][x][i] = 1

        while q:
            vd, vc, vy, vx = q.popleft()  # 이전 방향, 경로비용, y좌표, x좌표
            for i in range(4):
                ny, nx = vy + dy[i], vx + dx[i]

                if is_valid(ny, nx):
                    nd = i
                    nc = cost_cal(vd, nd, vc) if vd is not None else cost_cal(nd, nd, vc)
                    if ny == N - 1 and nx == N - 1:
                        if not visit[ny][nx][nd] or nc < visit[ny][nx][nd]:
                            visit[ny][nx][nd] = nc

                    elif not visit[ny][nx][nd] or nc < visit[ny][nx][nd]:  # 배열 처음 방문하는 경우
                        visit[ny][nx][nd] = nc
                        q.append((nd, nc, ny, nx))

    bfs(0, 0)
    answer = 999999999
    for i in range(4):
        temp = visit[-1][-1][i]
        if temp:
            answer = min(answer, temp)

    return answer