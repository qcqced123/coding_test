import sys
import heapq


def solution():
    """
    사탕을 누구에게 몇 개 분배할 것인가에 따라서 최적의 분노 수치가 달라지는데, 이걸 백트래킹으로 알아낼 수 도 없고
    그냥 현재 mid 값이 분노의 합의 최소값이 되려면, 사탕이 몇개 필요한가?? 그걸로 탐색 기준을 잡아??

    idea: parametric search
        - 최적화 대상/범위: 못 받는 사탕의 개수
        - 최적화 기준: 저게 나눠줄 수 있는 사탕 범위면 r을 줄이고, 나눠줄 수 없으면 l을 키우고

    question:
        - 최적화 대상 파라미터 정의가 안됨

    feedback:
        - 오히려 파라미터 정의는 잘했음, 근데 후처리 하는게 맞음, 저걸 도대체 어떻게 후처리하냐 에라이
        - 결국 골자는 파라매트릭 서치로 최대한 공평하게 사탕을 배분한 뒤, 남는 사탕을 어떻게 다시 배분해야
        - 남은 사탕은 이제 파라미터랑 차이가 가장 큰 쪽부터 분배

    reference:
        - https://konghana01.tistory.com/216
    """
    # get input data
    input = sys.stdin.readline
    M, N = map(int, input().split())
    expectations = [int(input()) for _ in range(N)]
    expectations.sort()

    # do parametric search
    remain = 0
    optimize = 0
    l, r = 0, max(expectations)
    while l <= r:
        cnt = 0
        avail = M
        mid = (l+r) // 2
        for expect in expectations:
            curr = max(expect-mid, 0)
            cnt += curr
            avail -= curr
            if cnt > M:
                break

        if cnt > M:
            l = mid + 1

        else:
            r = mid - 1
            remain = avail
            optimize = mid

    # assign remain candies
    q = []
    for i in range(N):
        if expectations[i] > optimize:
            M -= expectations[i] - optimize
            expectations[i] = optimize

        heapq.heappush(q, -expectations[i])

    while M:
        x = -heapq.heappop(q)
        heapq.heappush(q, -(x - 1))
        M -= 1

    print(sum([x ** 2 for x in q]) % 2 ** 64)


if __name__ == "__main__":
    solution()
