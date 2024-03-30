from itertools import combinations
from collections import Counter


def my_solution(orders, course):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/72411

    summary:
        1) 새로운 코스 요리 구성
            - 가장 많이 함께 주문한 단품 메뉴 (연관 규칙)
            - 코스: 최소 2개 이상의 단품, 최소 2명 이상의 손님에게 주문
    solution:
        1) O(N**2) 이하
            - itertools.Combination 이용해 course_dict 만들기
    return:
        1) 사전순서, 오름차순으로 정렬해서 리턴
        2) 개별 코스 길이 중에서, 최빈코스만 출력, 대신 동점이면 모두 출력
    """
    answer = []
    for k in course:
        course_dict = {}
        for n in orders:
            candidates = combinations(sorted(n), k)  # 이렇게 해줘야, WX, XW가 같은 것으로 인식
            for candidate in candidates:
                if candidate not in course_dict:
                    course_dict[candidate] = 1
                    continue
                course_dict[candidate] += 1

        course_dict = sorted(course_dict.items(), key=lambda x: x[1], reverse=True)
        if course_dict:
            max_order = course_dict[0][1]
            for k, v in course_dict:
                if v < 2 or v < max_order:
                    break
                answer.append(''.join(k))
    answer.sort()
    return answer


def solution(orders, course):
    """ itertools.combinations, collections.Counter"""
    answer = []
    for c in course:
        menu = []
        for order in orders:
            comb = combinations(sorted(order), c)
            menu += comb  # comb is a generator

        counter = Counter(menu)
        if len(counter) and max(counter.values()) > 1:
            for m, cnt in counter.items():
                if cnt == max(counter.values()):
                    answer.append("".join(m))
    return sorted(answer)