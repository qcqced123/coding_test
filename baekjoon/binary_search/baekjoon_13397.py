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
        lower, upper, cache = 0, 0, 0
        while lower <= upper < N:
            arr = numbers[lower:upper+1]  # 슬라이싱 떄문에 느린듯
            cnt = max(arr) - min(arr)
            if cnt <= mid:
                upper += 1

            else:
                lower = upper
                cache += 1

            if cache > M:
                break
        else:  # 여기가 핵심: 정상적으로 탐색된 경우, 마지막 구간은 구간 개수에 포함되지 않기 떄문에, 반영해줘야 함
            cache += 1

        if cache > M:
            l = mid + 1

        else:
            answer = mid
            r = mid - 1

    print(answer)


def solution2():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    answer = 0
    l, r = 0, max(numbers) - min(numbers)
    while l <= r:
        mid = (l+r) // 2
        lower, upper, cache = 0, 0, 0
        mini, maxi = numbers[0], numbers[0]
        while lower <= upper < N:
            new = numbers[upper]
            mini, maxi = new if new < mini else mini, new if new > maxi else maxi
            cnt = maxi - mini
            if cnt <= mid:
                upper += 1

            else:
                lower = upper
                mini = numbers[lower]
                maxi = mini
                cache += 1

            if cache > M:
                break
        else:
            cache += 1

        if cache > M:
            l = mid + 1

        else:
            answer = mid
            r = mid - 1

    print(answer)


if __name__ == "__main__":
    solution2()
