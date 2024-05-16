import sys
import copy


def solution(board, aloc, bloc):
    answer = 0

    def build_visit_arr(r: int, c: int):
        return [[[0, 0] for _ in range(c)] for _ in range(r)]

    visit = build_visit_arr(len(board), len(board[0]))

    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

    def is_valid(curr_y, curr_x):
        return

    def game_turn(grid, ay, ax, by, bx, turn):
        curr_board = copy.deepcopy(grid)

        for i in range(4):
            nay, nax = dy[i] + ay, dx[i] + ax
            if

    return answer