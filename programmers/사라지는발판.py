import copy


def solution(board, aloc, bloc):
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

    def is_valid(y, x, curr_y, curr_x, curr_grid):
        return curr_grid[y][x] and -1 < curr_y < len(curr_grid) and -1 < curr_x < len(curr_grid[0]) and \
            curr_grid[curr_y][curr_x]

    def game_turn(grid, ay, ax, by, bx):
        count, result = 0, 0
        curr_board = copy.deepcopy(grid)

        for i in range(4):
            nay, nax = dy[i] + ay, dx[i] + ax
            if is_valid(ay, ax, nay, nax, curr_board):
                count += 1
                for j in range(4):
                    nby, nbx = dy[i] + by, dx[i] + bx
                    if is_valid(by, bx, nby, nbx, curr_board):
                        count += 1
                        curr_board[ay][ax], curr_board[by][bx] = 0, 0
                        count += game_turn(curr_board, nay, nax, nby, nbx)
                        curr_board[ay][ax], curr_board[by][bx] = 1, 1  # backtracking
        return count

    answer = game_turn(board, aloc[0], aloc[1], bloc[0], bloc[1])
    return answer


if __name__ == '__main__':
    solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2])