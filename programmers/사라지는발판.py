import copy


def my_solution(board, aloc, bloc):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/92345

    implementation:
        1) 둘 다 이기는 걸 우선적으로 플레이하게 빌드
        2) 플레이어 움직인 횟수 판정하는게 힘들어
            - 무조건 맥스를 리턴하는게 아니구나, 그냥 누군가의 승리가 결정된 상황이면 리스트에 포함시키고 거기서 미니멈을 들고오자
        3) 누가 이겼는지 판정하는건 어떻게 할거야?
            - 내가 이동할 때는 괜찮았는데, 상대방 이동 때문에 갑자기 지는게 될 수도 있음 그래서 매 턴마다 현재 내가 서있는 칸의 상태를 확인해야함

        => 결국 최적의 플레이가 뭔지를 판정할 수가 없어서 이런 일이 벌어지는구만
        => 불나방 마냥 A가 있는곳으로 가버리니까 첫번째 예시 정답이 3이 나오네
    """
    answer = []
    row, col = len(board), len(board[0])
    dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

    def is_movable(grid, curr_y, curr_x) -> bool:
        """ function for judging current move state """
        return -1 < curr_y < row and -1 < curr_x < col and grid[curr_y][curr_x]

    def check_turn(turn: int) -> int:
        """ function for current turn (Player A or B) """
        return turn % 2

    def backtracking(grid, turn, count, ay, ax, by, bx):
        """
        0) validate the current position
        1) copy current state of board
        2) do the current turn
        3) move to next turn
        """
        # validate the current position
        # for player A, B
        if (not check_turn(turn) and not grid[ay][ax]) or (check_turn(turn) and not grid[by][bx]):
            answer.append(count)
            return

        # copy the current state of board
        # count the non-movable blocks of current turn
        cnt = 0
        curr_grid = copy.deepcopy(grid)
        for i in range(4):
            if not check_turn(turn):  # for player A
                ny, nx = dy[i] + ay, dx[i] + ax

            else:  # for player B
                ny, nx = dy[i] + by, dx[i] + bx

            # if is_movable return the False, it means that current moving state is incorrect
            # so, workflow will move to next iteration or updating the result of game
            if is_movable(curr_grid, ny, nx):
                if not check_turn(turn):  # for player A
                    curr_grid[ay][ax] = 0
                    backtracking(curr_grid, turn + 1, count + 1, ny, nx, by, bx)
                    curr_grid[ay][ax] = 1

                else:  # for player B
                    curr_grid[by][bx] = 0
                    backtracking(curr_grid, turn + 1, count + 1, ay, ax, ny, nx)
                    curr_grid[by][bx] = 1
            else:
                cnt += 1

        if cnt == 4:
            answer.append(count)

        return

    backtracking(board, 0, 0, aloc[0], aloc[1], bloc[0], bloc[1])
    return min(answer) if answer else 0


if __name__ == '__main__':
    print(my_solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]))