from typing import Tuple, List


def my_solution(want, number, discount):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/131127

    summary:
        1) 10일 회원 자격
            - 하루 한 가지 세일, 한 개 구매 가능
            - 원하는 품목, 수량이 할인 하는 날짜가 정확히 10일과 맞을 때 가입
    Args:
        want: 원하는 품목
        number: 품목 개수
        discount: 할인 계획

    Solution:
        1) O(N**2)이하
          - 하루마다 사전 초기화
          -
    """
    answer = 0
    for day in range(len(discount) - 9):
        curr = discount[day:day + 10]
        want_dict = {k: v for k, v in zip(want, number)}
        items = want_dict.keys()

        for item in curr:
            if item not in items:
                break
            want_dict[item] -= 1

        else:
            for v in list(want_dict.values()):
                if v > 0:
                    break
            else:
                answer += 1
    return answer


def solution(want, number, discount):
    """ 사전 비교 연산 활용 (collections.Counter 사용도 가능할 듯)
    """
    answer = 0
    want_dict = {k: v for k, v in zip(want, number)}

    for day in range(len(discount) - 9):
        curr = discount[day:day + 10]
        sale_dict = {k: 0 for k in curr}

        for item in curr:
            sale_dict[item] += 1

        if want_dict == sale_dict:
            answer += 1

    return answer