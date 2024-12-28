import sys
from bisect import bisect_left, bisect_right


def solution():
    """ 크기 작고, 색이 다른 공, 개별 플레이어 획득 가능한 크기 합, NlogN까지 가능
    idea: prefix sum
        - logN + N(logN + logN + logN)
        - 오름 차순 정렬: 정렬하되, 플레이어 번호까지 함께 저장
        - bisect_left, bisect__right 사용해서 lower bound, upper bound 인덱스 찾기
        - for i in range(lower, upper+1) 루프 돌리면서, 색상 확인

    """
    # get input data
    input = sys.stdin.readline
    N = int(input())
    cache = [0]*(N+1)
    arr = [[i+1] + list(map(int, input().split())) for i in range(N)]  # player, color, size
    arr.sort(key=lambda x: x[2])
    size = [i[2] for i in arr]  # array for bisecting

    # do bisect for finding lower bound & upper bound of current player
    for i, container in enumerate(arr):
        cnt_player, cnt_color, cnt_size = container
        l, u = bisect_left(size, cnt_size), bisect_right(size, cnt_size)
        print(cnt_player, cnt_color, cnt_size)
        print(l,u)
        print()

if __name__ == "__main__":
    solution()
