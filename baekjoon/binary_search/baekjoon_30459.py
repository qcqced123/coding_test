import sys
from bisect import bisect_left


def solution():
    """
    idea: prefix sum with bisect
    """
    # get input and sort
    input = sys.stdin.readline
    N, M, R = map(int, input().split())
    arr = list(map(int, input().split()))
    heights = list(map(int, input().split()))
    arr.sort(), heights.sort()

    # make prefix array (~밑변의 길이 경우의 수 배열)
    col = []
    prefix = []
    target = 2*R
    for i in range(N):
        cnt = arr[i]
        for j in range(i+1, N):
            case = 0
            temp = arr[j]
            if cnt < 0 and temp < 0: case += abs(cnt-temp)
            elif cnt < 0 and temp >= 0: case += abs(cnt) + temp
            elif cnt >= 0 and temp >= 0: case += temp-cnt
            col.append(case)
            prefix.append(target/case)

    # do bisect
    answer = 0
    size = len(col)
    for i in range(size):
        cnt_c, cnt_h = col[i], prefix[i]
        idx = bisect_left(heights, cnt_h)
        if idx == len(heights):
            idx -= 1

        if idx > 0 and heights[idx] > cnt_h:
            idx -= 1

        curr = round(cnt_c*heights[idx] / 2, 1)
        if curr <= R:
            answer = max(answer, curr)

    print(answer) if answer else print(-1)


if __name__ == "__main__":
    solution()
