from collections import deque
from typing import List


def my_solution(s: str):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/76502

    [요약]
    1) 올바른 괄호 문자열 만들기
    2) 왼쪽으로 s칸만큼 회전
        - 이 때, 열고 닫고 순서가 제대로 지켜진 애들 개수 세기
    [구현]
    O(N**2) 가능
    1) 길이만큼 루프
        - 회전: deque.rotate()
    2) 올바른 괄호 문자열인지 판정
        - dict 활용
        - 왼쪽 괄호 개수 >= 오른쪽 괄호 개수

    [결과]
    1) 85.7 / 100.0
        - 애초에 문제 이해에서 틀림
        - 나는 논리적 순서에 의해 제대로 열고 닫는지만 확인했는데, 그게 아니었네
        - ([)] => 이런 경우 나는 맞는 문자열이라고 생각했는데, 문제에 의하면 틀리다고 말해야함
        - 판정하는 알고리즘만 다시 짜면 되겠다
    """
    original = list(s)
    nums = len(original)

    answer = 0
    for x in range(nums):
        vocab = {'(': 0, ')': 0, '[': 0, ']': 0, '{': 0, '}': 0}
        flag = True
        curr = deque(original[:])
        curr.rotate(-x)
        while curr:
            vs = curr.popleft()
            vocab[vs] += 1

            cnt = vocab[vs]
            if vs == ')':
                if vocab['('] < cnt:
                    flag = False
                    break

            elif vs == ']':
                if vocab['['] < cnt:
                    flag = False
                    break

            elif vs == '}':
                if vocab['{'] < cnt:
                    flag = False
                    break
        if flag:
            answer += 1
    return answer


def solution(s: str):
    """ 올바른 문자열인지 판정하는 알고리즘 수정
    1) 나는 애초에 스택에 다 넣고 검사를 하려 했음
    2) 근데 문제 푸는거 보니까, 하나씩 차근차근 스택에 넣네
    """
    original = list(s)
    nums = len(original)

    answer = 0
    for x in range(nums):
        curr = deque(original[:])
        curr.rotate(-x)

        stack = []
        while curr:

            vs = curr.popleft()
            if vs == '(' or vs == '[' or vs == '{':
                stack.append(vs)

            else:
                if not stack:
                    break

                if vs == ')' and stack[-1] == '(':
                    stack.pop()

                elif vs == ']' and stack[-1] == '[':
                    stack.pop()

                elif vs == '}' and stack[-1] == '{':
                    stack.pop()

                else:
                    break
        else:
            if not stack:  # 스택이 완벽히 비어있어야 문제에서 말하는 올바른 괄호 문자열에 해당된다
                answer += 1
    return answer


