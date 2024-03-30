from collections import defaultdict


def solution(genres, plays):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/42579

    summary:
        1) 장르별 Top-2 재생 노래
            - key => plays 배열 인덱스
            1) 최다 재생 장르 고르기
            2) 장르별 Top-2 재생 노래
                - 동점, 고유 번호 낮은 노래부터
    args:
        노래 고유 번호 == plays 배열 인덱스

    solution:
        1) O(N**2) 이하
            - 장르 선정
            - 노래 선정 후, 배열에 담기
    returns:
        1) 인덱스가 담긴 리스트
    """
    counter = defaultdict(list)
    result, total = [], {k: 0 for k in set(genres)}

    for i, k in enumerate(genres):
        total[k] += plays[i]
        counter[k].append([plays[i], i])  # 재생횟수, 고유번호

    total = dict(sorted(total.items(), key=lambda x: x[1], reverse=True))
    for k in total.keys():
        counter[k].sort(key=lambda x: (x[0], -x[1]), reverse=True)
        curr = counter[k][0:2]
        for i in range(len(curr)):
            result.append(curr[i][1])
    return result
