import sys


def solution():
    """ 연속 구간 부분합, 최대값, M개 이하 구간
    적절하게 구간을 나눠서, 점수의 최대값의 최소값을 리턴

    idea: two pointer
        - 정렬 불가능
        - 점수의 최대: 점수 == 최대값 - 최소값
        - 탐색 대상/범위: 점수 배열, list(range(0, max-min+1))
        - 탐색 기준: 현재 점수랑, 해당 점수를 만드는데 필요한 구간의 개수 비교 (S)
            - 현재 점수보다 크면 구간 개수 추가
            - 구간 포인터 값 다시 세팅
    question:
        - 결국 연속 부분 배열의 점수가 기준이 되어야 하는데, 구간의 개수를 세어주는 기준을 못잡겠음
        -
    """
    input = sys.stdin.readline
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    answer = 0
    l, r = 0, max(numbers) - min(numbers)
    while l <= r:
        mid = (l+r) // 2
        cache = 0
        lower, upper = 0, 0
        while lower <= upper < N:
            arr = numbers[lower:upper+1]
            cnt = max(arr) - min(arr)
            if cnt < mid:
                upper += 1
            else:
                lower = upper
                cache += 1

            if cache > M:
                break

        if cache > M:
            r = mid - 1

        else:
            answer = mid
            l = mid + 1

    print(answer)


if __name__ == "__main__":
    solution()
