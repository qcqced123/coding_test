import sys
from bisect import bisect_left, bisect_right


def solution():
    """ NlogN, 석순: 바닥 to 천장, 종유석: 천장 to 바닥

    idea: binary search, two-pointer
        - 종유석, 석순 배열 나누기
        - 탐색 대상/범위: 장애물 개수, 0 to max
        - 탐색 기준:
    feedback:
        - 내가 이진 탐색 문제를 너무 편협하게 풀었구나,,,,
        - 뇌가 너무 어려운거에만 절여져서... 그냥 있는거 그대로 탐색하고, 풀면 되는데, 이런 유형도 염두해두고 풀자 이제
    """
    input = sys.stdin.readline
    N, H = map(int, input().split())  # 장애물 숫자, 길이
    up_list, down_list = [], []  # 석순, 종유석
    for i in range(N):
        cnt = int(input())
        if not i % 2: up_list.append(cnt)
        else: down_list.append(H-cnt)

    up_list.sort(), down_list.sort()  # 문제에서 길이 순서대로 준다는 조건이 없는데, 내가 창조함 ㅎ
    answer, subseq = sys.maxsize, 0
    for h in range(1, H+1):
        up, down = bisect_left(up_list, h), bisect_left(down_list, h)
        curr = N // 2 - up + down
        if curr < answer:
            answer = curr
            subseq = 1

        elif curr == answer:
            subseq += 1

    print(answer, subseq)


if __name__ == "__main__":
    solution()
