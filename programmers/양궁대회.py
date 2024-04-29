import sys
from typing import List


def solution(n, info):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/92342

    args:
        info: 어피치가 쏜 화살 결과
            - 인덱스: 과녁 점수
            - 원소값: 화살 숫자

        => 가장 큰 점수차로 라이언이 이기는 방법 찾기
        => info와 같은 포맷의 배열을 반환해야 한다

    solution:
        1) 화살 숫자 분배가 매우 중요
          - 몇개를 쏴서 이기던, 단일 점수만 획득 가능하기 때문

    implementation:
        0) 규칙:
          - 같은 화살 숫자: 무조건 어피치 승
          - 같은 점수: 무조건 어피치 승

        1) BackTracking
          - 모든 경우의 수를 탐색할 필요가 있음
    """
    lion, curr = [0] * 11, [0]
    sys.setrecursionlimit(10 ** 6)

    def compare(arr1: List, arr2: List) -> List:
        tmp = []
        for i in range(10, -1, -1):
            if arr1[i] > arr2[i]:
                return arr1
            elif arr2[i] > arr1[i]:
                return arr2

    def backtracking(src: int, score: int, remain: int, arr: List[int]) -> None:
        nonlocal lion
        if remain < 0 or src > 10:
            return

        if src == 10 and remain >= 0:  # and로 갈지 Or로 계속 갈지
            if remain: arr[src] = remain
            if score > curr[0]:
                lion, curr[0] = arr, score
            elif score == curr[0]:
                lion = compare(lion, arr)
            return

        arr[src] = info[src] + 1
        backtracking(src + 1, score + (10 - src), remain - arr[src], arr[:])  # 라이언이 해당 점수에서 이기는 경우

        arr[src] = 0
        if info[src]:
            backtracking(src + 1, score - (10 - src), remain, arr[:])
        else:
            backtracking(src + 1, score, remain, arr[:])

    backtracking(0, 0, n, [0] * 11)
    return [-1] if curr[0] < 1 else lion
