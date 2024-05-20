import math


def solution(board):
    """
    implementation:
        1) 세방향 중에서 제일 작은 값 찾기
        2) 모두 제일 작은 값 이상이라면, 한 사이즈 업
    """
    answer = 1
    R, C = len(board), len(board[0])

    def is_valid(curr_y, curr_x):
        return board[curr_y][curr_x] and board[curr_y - 1][curr_x] and board[curr_y][curr_x - 1] and board[curr_y - 1][
            curr_x - 1]

    for y in range(1, R):
        for x in range(1, C):
            if is_valid(y, x):
                size = min(board[y - 1][x], board[y][x - 1], board[y - 1][x - 1])
                area = (math.sqrt(size) + 1) ** 2
                answer = max(answer, area)
                board[y][x] = area

    if answer == 1:
        for i in range(R):
            for j in range(C):
                if board[i][j]:
                    return answer
        answer = 0
    return answer

