import sys


def solution():
    """
    idea: binary search
        - 탐색 대상/범위: 밟아야 하는 다리 개수, 1 to N
        - 탐색 조건

    feedback:
        - 1 to N 더하는 수식을 잘못알고 있었음
        - n(n-1)/2 가 아니라 n(n+1)/2 이었음... ㅋㅋㅋㅋㅋㅋㅋㅋ
        - 시작하는 징검다리의 위치값이 커질수록 밟을 수 있는 징검다리 개수가 작아지기 때문에 시작 위치는 항상 1부터 시작하는 것도 잘 생각함
        - 근데 햇갈렸던게, 이진 탐색 배열의 원소값을 건너야할 징검다리로 잘 해석해놓고, 위에 팩트도 잘잡았는데 이를 잘 연결을 못함
        - 두 사실을 연결 지으면, 이분 탐색 배열의 원소값은 건너야할 징검다리의 개수이자, 마지막 징검다리의 위치값이라고 해석할 수도 잇음
    """
    input = sys.stdin.readline
    test = [int(input()) for _ in range(int(input()))]
    for t in test:
        answer = 0
        l, r = 1, t
        while l <= r:
            mid = (l+r) // 2  # 건너야 할 징검다리 개수로 해석
            if mid*(mid+1) // 2 <= t:
                answer = mid
                l = mid + 1

            else:
                r = mid - 1

        print(answer)


if __name__ == "__main__":
    solution()
