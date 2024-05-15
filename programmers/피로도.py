import sys
from typing import List


def solution(k, dungeons):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/87946?language=python3

    solution:
        1) 최소 필요 피로도
        2) 소모 피로도
        => 최대한 많은 던전 탐험하기

    implementation:
        1) Backtracking

    """
    answer = [0]
    sys.setrecursionlimit(10 ** 6)

    def backtracking(src: int, candidates: List, result: int):
        for i in range(len(candidates)):
            lower_bound, consume = candidates[i]
            if src >= lower_bound:
                backtracking(src - consume, candidates[:i] + candidates[i + 1:], result + 1)

        answer[0] = max(answer[0], result)

    backtracking(k, dungeons, 0)
    return answer[0]


if __name__ == '__main__':
    solution(100, [[100, 100], [100, 100], [100, 100], [100, 100], [100, 100]])