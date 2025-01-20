import sys
from bisect import bisect_left, bisect_right


def solution():
    """ NlogN
    idea: prefix sum with bisect
        - sort by ending time
        - 이분 탐색 이용, 현재 강의의 "시작 시간"과 가장 근처에 "끝나는 강의" 찾기
        - prefix[i]: i분 까지의 최대 인원수
    """
    # get input data
    input = sys.stdin.readline
    N = int(input())
    information = [list(map(int, input().split())) for _ in range(N)]
    information.sort(key=lambda x: (x[1], x[0], x[2]))

    # init the prefix array, starting array, end array
    prefix = [0]*N
    start_list = [information[i][0] for i in range(N)]
    end_list = [information[i][1] for i in range(N)]
    people = [information[i][2] for i in range(N)]

    # find the latest lecture with bisect
    lectures = [0]*N
    for i in range(N):
        cnt = start_list[i]
        lectures[i] = bisect_right(end_list, cnt) - 1

    # update prefix sum array
    for i in range(N):
        curr = 0
        if lectures[i] > -1:
            curr += prefix[lectures[i]]

        prefix[i] = max(prefix[i-1], curr + people[i])

    # answering the question
    print(max(prefix))


if __name__ == "__main__":
    solution()
