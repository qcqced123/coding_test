import sys
from typing import List, Tuple
from collections import deque
"""
[요약]
1) 구현
    - 시간, 메모리, 입력 길이: 1초, 512, 1000
    - row, col, weight, speed, direction = inputs
    - grid[i][j]: [count, sum_weight, sum_speed, direction]
    - ball_info: queue로 구현
"""


def split_ball(y: int, x: int, graph: List[List[List[int]]], q: deque):
    """ split ball into 4 balls in specific grid, which is over-lap more than two """
    count, weight, speed, direction = graph[y][x]
    if count > 1:
        weight, speed, direction = weight // 5, speed // count, [0, 2, 4, 6] if not direction or count == direction else [1, 3, 5, 7]
        for i in range(4):
            if weight:
                q.append([y, x, weight, speed, direction[i]])
    elif count == 1:
        q.append([y, x, weight, speed, direction])


def grid_calculate(row: int, col: int, graph: List[List[List[int]]], data: List[int]) -> None:
    """ update ball's infor in specific grid index after one-iteration
    Args:
        graph: grid
        data: ball_info
    """
    _, _, weight, speed, direction = data
    if not graph[row][col]:
        graph[row][col] = [1, weight, speed, direction]
    else:
        graph[row][col][0] += 1  # update count value
        graph[row][col][1] += weight  # update weight value
        graph[row][col][2] += speed  # update speed value
        graph[row][col][3] += direction % 2  # update direction value


def move(data: List[int]) -> Tuple[int, int]:
    """ abstraction for one-iteration """
    dy, dx = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]  # row, col direction
    row, col, m, s, d = data
    ny, nx = dy[d] * s, dx[d] * s
    n_row, n_col = row + ny, col + nx

    # 그리드 밖으로 나가는 경우 처리
    if n_row < 1:
        n_row = N - (n_row % N)
    elif n_col < 1:
        n_col = N - (n_col % N)

    if n_row > N:
        if not n_row % N:
            n_row = N
        else:
            n_row = n_row % N
    elif n_col > N:
        if not n_col % N:
            n_col = N
        else:
            n_col = n_col % N
    return n_row, n_col


# 1) init values
N, M, K = map(int, sys.stdin.readline().split())  # grid_size, num of fireball, iter
queue = deque([])

for _ in range(M):
    queue.append(list(map(int, sys.stdin.readline().split())))

for _ in range(K):
    # 2) move each fireball one iter, count same position
    pos_ball = []
    grid = [[0] * (N + 1) for _ in range(N + 1)]  # grid[row][col] = [count, weight, speed, direction]
    while queue:
        ball_info = queue.popleft()
        new_row, new_col = move(ball_info)  # update fire ball position
        grid_calculate(new_row, new_col, grid, ball_info)  # update count value in grid
        if not [new_row, new_col] in pos_ball:
            pos_ball.append([new_row, new_col])

    # 3) split ball into 4 unique balls
    for i in range(len(pos_ball)):
        y, x = pos_ball[i]
        split_ball(y, x, grid, queue)

# 4) calculate result
result = 0
for i in range(len(queue)):
    result += queue[i][2]
print(result)






