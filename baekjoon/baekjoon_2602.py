import sys


def solution():
    """
    idea: backtracking
        - 인자 정의: 현재 탐색 대상 글자, 현재 탐색 대상 x 좌표, 현재 밟아야 하는 다리 타입
        - 탐색 대상: 스택 외부(시퀀스), 스택 내부(다리)
    """
    # backtrack func
    def backtrack(cnt_s, cnt_x, cnt_t) -> None:
        """
        Args:
            cnt_s: 현재 탐색 대상 글자
            cnt_x: 현재 탐색 대상 x 좌표
            cnt_t: 현재 밟아야 하는 다리 타입
        """
        # end point of stack
        nonlocal answer
        if cnt_s == len(sequence):
            answer += 1
            return

        # find the next character
        for k in range(cnt_x+1, len(grid[0])):
            # find the next node in 1
            if not cnt_t and sequence[cnt_s] == grid[1][k]:
                backtrack(cnt_s+1, k, 1)

            elif cnt_t and sequence[cnt_s] == grid[0][k]:
                backtrack(cnt_s+1, k, 0)

    # get the input
    input = sys.stdin.readline
    sequence = input().rstrip()
    grid = [list(input().rstrip()) for _ in range(2)]

    # do backtrack
    answer = 0
    for i in range(2):
        for j in range(len(grid[0])):
            if grid[i][j] == sequence[0]:
                backtrack(1, j, i)

    print(answer)


def solution2():
    """
    idea: dynamic programming
        - 입력 길이 보고, backtracking 생각 했는데... 낚시였다
    """
    # get the input
    input = sys.stdin.readline
    sequence = input().rstrip()
    grid = [list(input().rstrip()) for _ in range(2)]

    x_size = len(grid[0])
    cache = [[0]*x_size for _ in range(2)]

    # update the dp cache
    for x in range(x_size):
        for y in range(2):
            pass

    return


if __name__ == "__main__":
    solution2()
