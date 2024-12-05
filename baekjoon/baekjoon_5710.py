import sys


def solution():
    """ 상근이가 사용한 전기량을 귀납적으로 찍기
    idea: binary search
        - 요금 범위 테이블 만들기
        - A를 요금 범위 테이블을 이용해, 몇 와트 사용했는지로 바꾸기
        - 탐색 대상/범위: 상근이가 사용한 전기량, 0 to 이웃과 상근이 전기 사용량 합

    feedback:
        - 왜 틀렸지...

    """
    def calculate_cost(watt: int) -> int:
        cost = 0
        temp = [100, 9900, 990000, INF]
        for i, v in enumerate(temp):
            if watt > v:
                watt -= v
                cost += v*weights[i]

            else:
                cost += watt*weights[i]
                break
        return cost

    INF = sys.maxsize
    input = sys.stdin.readline
    while True:
        A, B = map(int, input().split())
        if not A and not B:
            break

        # divide A into sum of sub element
        weights = [2, 3, 5, 7]
        watt_table = [100, 10000, 1000000, INF]
        cost_table = [200, 29900, 4970100, INF]

        idx = 0
        total = 0
        for i in range(4):
            if cost_table[i] > A:
                idx += i
                break
        if idx:
            total += watt_table[idx-1]
            A -= cost_table[idx-1]

        total += A // weights[idx]

        # # do bisect
        answer = INF
        l, r = 1, total
        while l <= r:
            mid = (l+r) // 2
            cnt = total - mid
            X, Y = calculate_cost(cnt), calculate_cost(mid)
            curr = abs(X-Y)
            if curr > B:
                l = mid + 1

            else:
                r = mid - 1
                answer = min(answer, X, Y)

        print(answer)


if __name__ == "__main__":
    solution()
