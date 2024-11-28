import sys
from bisect import bisect_left


def solution():
    """
    idea: 부분합 with bisect
        - 학급 마다 부분합 배열 만들기
        - 무게 순으로 오름 차순 정렬

    feedback:
        - 누적합으로 어찌저찌 풀었는데, 다른 방식이 있나 찾아보자
    """
    # init the data structure
    INF = sys.maxsize
    input = sys.stdin.readline

    for _ in range(int(input())):
        k, n = map(int, input().split())  # 기준 무게, 학급의 학생 숫자
        students = [list(map(int, input().split())) for _ in range(4)]

        # make the sub sequence's sum array
        group_a = []
        group_b = []
        for i in range(n):
            for j in range(n):
                group_a.append(students[0][i] + students[1][j])
                group_b.append(students[2][i] + students[3][j])

        # do sort by ascending
        group_a.sort()
        group_b.sort()

        # do bisect
        result = INF
        answer = INF
        for candidate in group_a:
            lookup = k - candidate
            idx = bisect_left(group_b, lookup)
            if idx >= len(group_b):
                idx -= 1

            curr1 = abs(k - (candidate+group_b[idx]))
            curr2 = abs(k - (candidate+group_b[idx-1]))

            if curr1 < curr2:
                curr = curr1

            elif curr2 < curr1:
                curr = curr2
                idx -= 1

            else:
                curr = curr1
                if candidate+group_b[idx-1] < candidate+group_b[idx]:
                    idx -= 1

            if curr <= answer:
                if curr == answer: result = min(result, candidate+group_b[idx])
                else: result = candidate+group_b[idx]
                answer = curr

        print(result)


if __name__ == "__main__":
    solution()
