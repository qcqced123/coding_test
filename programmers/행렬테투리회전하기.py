import copy


def my_solution(rows, columns, queries):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/77485

    summary:
        1) sub_rectangle의 테두리 부분에 있는 숫자 선택
            - (x1, y1, x2, y2): x가 행, y가 열을 의미함
            - 실제 구현할 때는 뒤집어서 생각하자
            - 테이블 인덱스 != 좌표값

        2) 시계방향으로 회전
            - 한 칸씩

    args:
        queries: 선택 범위, 회전 횟수
    """
    RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3
    dy, dx = (0, 1, 0, -1), (1, 0, -1, 0)

    answer = []
    table = [[rows * r + c + 1 for c in range(columns)] for r in range(rows)]
    for query in queries:
        sy, sx, ey, ex = [i - 1 for i in query]  # 인덱스 조심
        curr = copy.deepcopy(table)  # 쿼리 반영 테이블

        curr_height, curr_width = ey - sy + 1, ex - sx + 1  # 서브 테이블의 세로, 가로
        edges = curr_height * 2 + (curr_width - 2) * 2
        temp, count, vd = 999999999999, 0, RIGHT
        while edges != count:
            if vd == RIGHT and count == curr_width - 1:
                vd = (vd + 1) % 4

            elif vd == DOWN and count == curr_width + curr_height - 2:
                vd = (vd + 1) % 4

            elif vd == LEFT and count == curr_width + curr_height + curr_width - 3:
                vd = (vd + 1) % 4

            elif vd == UP and count == curr_width + curr_height + curr_width + curr_height - 4:
                vd = (vd + 1) % 4

            ny, nx = dy[vd] + sy, dx[vd] + sx
            curr[ny][nx] = table[sy][sx]

            temp = min(temp, table[sy][sx])
            sy, sx = ny, nx
            count += 1

        table = curr
        answer.append(temp)

    return answer


def solution1(rows, columns, queries):
    """
    solution:
        1) anti-clockwise
    """
    answer = []
    table = [[columns*r + c + 1 for c in range(columns)] for r in range(rows)]  # 정사각행렬이 아니다
    for query in queries:
        sy, sx, ey, ex = [i-1 for i in query]  # 인덱스 조심

        # 왼쪽 세로
        cache = table[sy][sx]
        min_value = cache
        for y in range(sy, ey):
            table[y][sx] = table[y+1][sx]
            min_value = min(min_value, table[y+1][sx])

        # 아래 가로
        for x in range(sx, ex):
            table[ey][x] = table[ey][x+1]
            min_value = min(min_value, table[ey][x+1])

        # 오른쪽 세로
        for y in range(ey, sy, -1):
            table[y][ex] = table[y-1][ex]
            min_value = min(min_value, table[y-1][ex])

        # 위 가로
        for x in range(ex, sx+1, -1):
            table[sy][x] = table[sy][x-1]
            min_value = min(min_value, table[sy][x-1])

        table[sy][sx+1] = cache
        answer.append(min_value)
    return answer


def solution2(rows, columns, queries):
    """
    solution:
        1) anti-clockwise with optimize by slicing
    """
    answer = []
    table = [[columns * r + c + 1 for c in range(columns)] for r in range(rows)]  # 정사각행렬이 아니다
    for query in queries:
        sy, sx, ey, ex = [i - 1 for i in query]  # 인덱스 조심
        row1, row2 = table[sy][sx:ex], table[ey][sx + 1:ex + 1]
        min_value = min(row1 + row2)

        for y in range(ey, sy, -1):
            table[y][ex] = table[y - 1][ex]
            min_value = min(min_value, table[y - 1][ex])

        for y in range(sy, ey):
            table[y][sx] = table[y + 1][sx]
            min_value = min(min_value, table[y + 1][sx])

        table[sy][sx + 1:ex + 1], table[ey][sx:ex] = row1, row2
        answer.append(min_value)

    return answer