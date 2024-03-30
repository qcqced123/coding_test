from collections import defaultdict


def solution(id_list, report, k):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/92334

    summary:
        1) 불량 이용자 신고, 처리 결과 메일로 자동 발송
            - 한번에 한 건씩 처리
            - 한 유저 여러번 고소 가능, 그러나 모두 1회로 간주
            - 서로 다른 유저에게 k번 이상 신고, 해당 유저 정지
                - 정지: 신고한 모든 유저에게 결과 발송
    args:
        report: 신고 유저, 신고 당한 유저
        k: 정지 기준

    solution:
        1) O(id_list*report)
            - 사전 두 개 준비

    """
    point_dict, pointed_dict = {i: 0 for i in id_list}, defaultdict(set)
    for context in report:
        pointer, pointed = context.split()
        pointed_dict[pointed].add(pointer)

    for i, j in pointed_dict.items():
        if len(j) >= k:
            for z in j:
                point_dict[z] += 1
    answer = list(point_dict.values())
    return answer