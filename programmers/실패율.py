from typing import List


def my_solution(N: int, stages: List[List]):
    """
    Problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/42889

    Solution 1. O(N*M)
      0) 유저에 따라 게임 시간 늘리기
        - 실패율 구하기
        - 도달 but 클리어 못한 사람 / 도달한 플레이어 수 (분자+성공)

      1) 스테이지 별, 실패율 구하기

      2) 내림차순으로 스테이지 번호 정렬

    => 통과는 하지만, 너무 비효율적인 풀이, 가장 긴 입력일 때 거의 10초 가까이 나옴
    => 이중 리스트의 경우는 리스트 곱으로 반복하면 안된다. 원소가 리스트라서, 모든 인덱스의 원소가 동일한 주소를 갖고,
       리스트가 mutable 객체라는 점을 감안하면, 수정이 일어나도, 복사가 일어나지 않아서, 모든 원소가 동일한 값을 갖게 된다
    """
    curr = [[0, 0] for _ in range(N + 1)]  # 분자, 분모
    for i, j in enumerate(stages):  # 20만
        for k in range(1, j):
            curr[k][1] += 1

        if j == N + 1:
            continue

        curr[j][0] += 1
        curr[j][1] += 1

    answer = {i: 0 for i in range(1, N + 1)}
    for stage in range(1, N + 1):
        ing, total = curr[stage]
        if total:
            answer[stage] = ing / total
        else:  # if not total, it maybe raise runtime error
            answer[stage] = 0

    answer = [i for i, j in sorted(answer.items(), key=lambda x: x[1], reverse=True)]
    return answer


def solution(N, stages):
    """ 스테이지는 순차적으로 진행된다는 점을 이용하면, O(N*M) 풀이가 아니라도 풀 수 있다,
    꼭 명심하자 이 문제
    """
    challenger = [0]*(N+2)
    for stage in stages:
        challenger[stage] += 1

    fails = {}
    total = len(stages)
    for i in range(1, N+1):
        if challenger[i] == 0:
            fails[i] = 0
        else:
            fails[i] = challenger[i] / total
            total -= challenger[i]  # 이렇게 푸니까 훨씬 빠르다
    result = sorted(fails, key=lambda x: fails[x], reverse=True)
    return result
