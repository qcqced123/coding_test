import sys
from collections import Counter


def solution():
    """ 그냥 연속 인형 수열에 K개 이상의 라이언 인형만 포함 되면 되는데, 그 중에서 가장 작은 집합의 크기
    그럼 계속 줄여나가면 되겠구나
    이거 sliding window + two pointer 풀었던거랑 똑같네

    idea: two pointer
        0) 초기값 설정
        1) 포인터 정보 초기화
            - 포인터 위치: 나란히
            - 포인터 방향: forward
            - 포인터 이동 조건:
                - 일단 K를 만족할 떄까지 쭉 오른쪽만 이동
                - K 만족하는 순간, 현재 왼쪽 포인터를 오른쪽으로 이동가능한지 판정하기, 못움직이면 다시 오른쪽만 움직이자

    개수가 적을 떄:
        오른쪽 포인터만 이동

    개수가 같을때:
        - 현재 왼쪽 포인터 값이 2: 왼쪽 포인터 옮기기
        - 현재 왼쪽 포인터 값이 1: 안옮기고, 오른쪽 옮기기

    개수가 많을 떄

    1 2 2 2 1 2 1 2 2 1
                      0
            0         0
    """
    N, M = map(int, sys.stdin.readline().split())
    dolls = list(map(int, sys.stdin.readline().split()))

    l, r = 0, 0
    result = 1e+10

    lion = 1 if dolls[l] == 1 else 0


if __name__ == "__main__":
    solution()
