import sys


def solution():
    """ 상근이가 사용한 전기량을 귀납적으로 찍기
    idea: binary search
        - A 값으로 이웃과 상근이 전기 사용량 역추적
        - 탐색 대상/범위: 상근이 전기 사용량, 0 to total
    """

    def get_wh_from_bill(bill):
        arr = [100 * 2, 100 * 2 + 9900 * 3, 100 * 2 + 9900 * 3 + 990000 * 5]

        if bill <= arr[0]:
            return bill // 2
        if bill <= arr[1]:
            return 100 + (bill - arr[0]) // 3
        if bill <= arr[2]:
            return 10000 + (bill - arr[1]) // 5

        return 1000000 + (bill - arr[2]) // 7

    def get_bill_from_wh(wh):
        arr = [100, 10000, 1000000]

        if wh < arr[0]:
            return wh * 2
        if wh < arr[1]:
            return 100 * 2 + (wh - 100) * 3
        if wh < arr[2]:
            return 100 * 2 + 9900 * 3 + (wh - 10000) * 5
        return 100 * 2 + 9900 * 3 + 990000 * 5 + (wh - 1000000) * 7

    INF = sys.maxsize
    input = sys.stdin.readline
    while True:
        A, B = map(int, input().split())
        if not A and not B:
            break

        # do bisect
        answer = INF
        total = get_wh_from_bill(A)
        l, r = 1, total
        while l <= r:
            mid = (l+r) // 2
            cnt = total - mid
            X, Y = get_bill_from_wh(mid), get_bill_from_wh(cnt)
            curr = abs(X-Y)
            if curr > B:
                l = mid + 1

            elif curr < B:
                r = mid - 1

            else:
                answer = min(answer, X, Y)
                break

        print(answer)


if __name__ == "__main__":
    solution()
