from typing import List


def my_solution(board: List[List[int]], moves: List[int]):
    """
    problem link:
       https://school.programmers.co.kr/learn/courses/30/lessons/64061

    summary:
       1) 인형뽑기
         - 바구니: stack
            - 크기 제한 x
         - 같은 모양 인형 두 개 연속: 폭발
         - 사라진 인형 개수 세기

    implementation:
        1) O(N*M)
        2) stack 사용
    """
    answer, stack = 0, []
    for move in moves:
        for row in range(len(board)):
            if not board[row][move - 1]:  # empty space
                continue

            if not stack or stack[-1] != board[row][move - 1]:  # stack push
                stack.append(board[row][move - 1])
                board[row][move - 1] = 0
                break

            elif stack and stack[-1] == board[row][move - 1]:
                stack.pop()
                answer += 2
                board[row][move - 1] = 0
                break

    return answer