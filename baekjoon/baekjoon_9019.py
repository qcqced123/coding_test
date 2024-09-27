import sys
from collections import deque


def solution():
    """ 십진수 저장 (최대 4자리)
    주어진 규칙에 맞게 숫자 변환 (Backtracking)

    A to B, 최소 명령어 나열 (명령어 시퀀스 길이 기준 업데이트)

    idea: back tracking
        1) L & R: deque rotate() 사용
        2) 숫자 자리수 유지 위해서 (0110 -> 110) 더미값 사용

    """
    def get_register():
        return

    def recursive_func():
        return

    dummy = 100000
    N = int(input())
    sys.setrecursionlimit(10**4)
    register = ["D", "S", "L", "R"]
    for _ in range(N):
        src, end = map(int, sys.stdin.readline().split())  # dtype must be int


if __name__ == "__main__":
    solution()
