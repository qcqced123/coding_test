import sys


def solution():
    """ 시험지 순서, 부분합, NlogN
    idea: two-pointer, binary search, 부분합
        - 정상적으로 탐색해서는 시간 복잡도 맞출 수 없기 떄문에, 역으로 추론
        - 구간 나누기 문제랑 비슷
        - 탐색 대상/범위: 점수 배열, 0 to sum
        - 탐색 기준: 현재 점수를 최대 점수로 만드는데 필요한 구간의 개수 (T)
            - 구간 개수가 많아질수록 최대값은 작아짐
            - 구간 개수가 적어질수록 최대값은 커짐
            - T > S: l forward
            - T <= S: r backward
    question:
        - 인덱스 에러가 왜 날까....?
    """
    input = sys.stdin.readline
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    # edge case handling
    if N == K:
        print(min(numbers))
        return

    answer = 0
    l, r = min(numbers), sum(numbers)
    while l <= r:
        mid = (l + r) // 2  # 현재 기준 점수
        cache = 0
        cnt, lower, upper = numbers[0], 0, 0
        while lower <= upper < N - 1:
            tmp = cnt + numbers[upper + 1]
            if tmp < mid:
                cnt = tmp
                upper += 1

            elif cache < K - 1:
                cache += 1
                upper += 2
                lower = upper
                cnt = numbers[lower]

            else:
                cnt = sum(numbers[lower:])
                break

        if cnt < mid:
            r = mid - 1

        else:
            answer = mid
            l = mid + 1

    print(answer)


if __name__ == "__main__":
    solution()
