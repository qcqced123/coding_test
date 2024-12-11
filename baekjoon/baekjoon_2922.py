import sys


def solution():
    """
    idea: dynamic programming
        - 즐거운 단어: 모음 3연속, 자음 3연속 x, L 포함
        - 빈 칸이 여러 개인 경우 캐싱 필요
        - structure: len(string)*nums of empty
    """
    input = sys.stdin.readline
    string = list(input().rstrip())
    


if __name__ == "__main__":
    solution()
