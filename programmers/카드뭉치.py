from typing import Tuple, List
from collections import deque


def my_solution(cards1, cards2, goal):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/159994

    summary:
        1) 원하는 순서의 단어 배열 만들기
          - 순서대로 한 장씩 사용
          - 한 번 쓰면 다시 못 써
          - 뽑은건 써야함
          - 이미 만든 배열 순서 못 바꿈
    Args:
        goal: 목표 배열

    solution:
        1) 큐 포인터로 구현
    """
    f_pointer, s_pointer, g_pointer = 0, 0, 0
    len_f, len_s, len_g = len(cards1), len(cards2), len(goal)

    while g_pointer <= len_g - 1:
        if f_pointer < len_f and cards1[f_pointer] == goal[g_pointer]:
            f_pointer += 1
            g_pointer += 1

        elif s_pointer < len_s and cards2[s_pointer] == goal[g_pointer]:
            s_pointer += 1
            g_pointer += 1

        else:
            break
    answer = 'Yes' if g_pointer > len(goal) - 1 else 'No'
    return answer


def solution(cards1, cards2, goal):
    """
    1) 실제 큐 동작 구현한 방법
    """
    cards1, cards2, goal = deque(cards1), deque(cards2), deque(goal)
    while goal:
        if cards1 and cards1[0] == goal[0]:
            cards1.popleft(), goal.popleft()

        elif cards2 and cards2[0] == goal[0]:
            cards2.popleft(), goal.popleft()

        else: break

    answer = 'Yes' if not goal else 'No'
    return answer
