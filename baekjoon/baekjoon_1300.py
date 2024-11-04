import sys


def solution():
    """ 2차원 테이블: 행*열 인덱스 값, 10억, N
    2차원 테이블 to 1차원 테이블 flat, top-k번째 원소 출력

    idea: binary search, two-pointer
        - 탐색 대상/범위: 계산 결과 나열한 배열 (직접 계산은 x)
        - 포인터 이동 기준: 현재 계산값 vs K 비교
        - 현재 계산값이 전체에서 몇 번째 숫자인지 어떻게 구함? (이게 상수 시간에 가능함??)

    question:
        - 현재 계산값이 배열에서 몇 번쨰 숫자인지 구하는 알고리즘... 모르겠음
    """
    input = sys.stdin.readline
    N = int(input())
    K = int(input())

    arr = list(range(N**2+1))


if __name__ == "__main__":
    solution()
