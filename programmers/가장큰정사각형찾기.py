import math


def my_solution(board):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/12905

    solution:
        1)

    implementations:
        1) 1행, 1열 넘기기
        2) 현재 순회하는 행번호의 제곱 만큼이 최대 넓이
          - 왼쪽 대각선, 왼쪽, 위: 이렇게 3방향이 모두 이전 행번호 제곱과 같으면 넓이는 현재 행번호 제곱
    """
    N, M = len(board), len(board[0])
    answer = 1
    for y in range(1, N):
        prev_max = y ** 2
        for x in range(1, M):
            if not board[y][x]:
                continue

            UP, LEFT_UP, LEFT = board[y - 1][x], board[y - 1][x - 1], board[y][x - 1]
            if UP and LEFT_UP and LEFT:
                if UP >= prev_max and LEFT_UP >= prev_max and LEFT >= prev_max:
                    board[y][x] = int((y + 1) ** 2)
                    answer = max(answer, board[y][x])
                else:
                    scalar = math.sqrt(min(UP, LEFT_UP, LEFT)) + 1
                    board[y][x] = int(scalar ** 2)
    return answer


def solution(board):
    pass


if __name__ == '__main__':
    my_solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]])
