import sys


def solution():
    """ NlogN, 시간 복잡도 떄문에, 최소 인출 금액을 귀납적으로 찍어서 맞추는게 빠름
    idea: binary search
        - 탐색 대상/범위: 인출 금액 배열, 0 to 10000
        - 탐색 조건: 기준 금액을 '최소'의 인출 금액으로 만드는데 필요한 인출 횟수 (S)
            - S > M: l = mid + 1
            - S <= M: r = mid - 1, 정답 기록

    feedback:
        - "정확히 M번을 맞추기 위해서 남은 금액이 그날 사용할 금액보다 많더라도 남은 금액은 통장에 집어넣고 다시 K원을 인출할 수 있다"라는 언급 때문에 복잡하게 생각함
            - 할 수도 있다라서, 안해도 되는거구나

    """
    # init the data structure
    INF = sys.maxsize
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = [int(input()) for _ in range(N)]

    # do the bisect
    answer = 0
    maxi = max(arr)
    l, r = 1, sum(arr)
    while l <= r:
        mid = (l+r) // 2
        cnt, pull = mid, 1
        for cost in arr:
            if cnt < cost:
                cnt = mid
                pull += 1

            cnt -= cost

        if pull > M or mid < maxi:
            l = mid + 1

        else:
            answer = mid
            r = mid - 1

    print(answer)


if __name__ == "__main__":
    solution()
