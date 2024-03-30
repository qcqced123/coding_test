from typing import Tuple, List


def my_solution(participant: List[str], completion: List[str]) -> str:
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/42576

    summary:
        1) 완주하지 못한 한 명 찾기
            - 동명이인 존재(이거 처리를 어떻게 하냐)

    Args:
        participant: 참가자 이름 배열
        completion: 완주한 사람

    Solution:
        1) O(NlogN) 이하
          - 사전 만들기, 동명이인 처리용, 완주한 사람 기록용
          - completion 순회하며 사전 업데이트
          - 사전 순회
          - 동명이인 때문에 세트 사용 x
    """
    people_dict = {k: [0, 0] for k in participant}
    for people in participant:
        people_dict[people][0] += 1

    for key in completion:
        people_dict[key][1] += 1

    answer = ''
    for key, value in people_dict.items():
        if value[0] > value[1]:
            answer = key
            break

    return answer

