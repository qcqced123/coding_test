import sys


def solution():
    """
    idea: binary search
        - 탐색 대상/범위: 마지막 상자 번호, min(전체 규칙) to max(전체 규칙)
        - 탐색 조건: 현재 상자 번호가 마지막 상자 번호일 떄, 숨긴 도토리 개수(S)
            -
    """
    # init data structure
    INF = sys.maxsize
    input = sys.stdin.readline
    N, K, D = map(int, input().split())  # 상자, 규칙, 도토리

    rules = []
    l, r = INF, 0
    for _ in range(K):
        src, end, step = map(int, input().split())
        l = min(l, src)
        r = max(r, end)
        rules.append((src, end, step))

    rules.sort()

    # do bisect
    answer = 0
    while l <= r:
        cnt = 0
        mid = (l+r) // 2
        for src, end, step in rules:
            if src > mid:
                continue
            # 애초에 정렬도 하고, 이분 탐색 배열 범위도 주어진 룰의 양끝으로 세팅해서 이 조건이 굳이 필요할까 싶었는데
            # 생각해보면, 이분 탐색 과정에서 mid가 엄청 왔다 갔다하면서 현재 규칙의 end보다 클 가능성도 당연히 있겠구나
            if end < mid:
                cnt += ((end-src) // step) + 1

            else:
                cnt += ((mid-src) // step) + 1

            if cnt >= D:
                break

        if cnt >= D:
            answer = mid
            r = mid - 1

        else:
            l = mid + 1

    print(answer)


if __name__ == "__main__":
    solution()
