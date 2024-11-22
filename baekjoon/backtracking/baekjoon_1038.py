import sys
from itertools import combinations


def solution():
    """ N번째 감소 하는 숫자 찾기!
    근데 앞에 자리 추가하는건 도대체 어떻게 할까...?
    idea: backtracking
        - 논리구조가 진짜 이쁜듯... 우와
    """
    input = sys.stdin.readline
    N = int(input())
    answer = []
    for i in range(1, 11):
        for j in combinations(list(range(10)), i):
            num = sorted(list(j), reverse=True)
            answer.append(int("".join(map(str, num))))

    answer.sort()
    try:
        print(answer[N])
    except:
        print(-1)


if __name__ == "__main__":
    solution()
