import sys


def solution():
    """ 더 작은 번호 쪽부터 채우기, 줄의 마지막 아이가 타게 되는 기구 번호
    idea: parametric search
        - 검색대 문제랑 똑같은데, 마지막 놀이 기구를 어떻게 찾아??
        - 최적 시간을 찾으면, 구할 수 있는지 확인해보자
        - 최적화 대상/범위:
        - 최적화 기준: 현재 기준 시간 동안, 몇 명을 태울 수 있을까??
            - 인원수 += 시간 // 기구별 시간

    question:
        - 모두 태우는데 필요한 최소 시간은 구할 수 있음
        - 최소 시간값으로, 어떻게 해보면 마지막 기구의 위치값을 알 수 있을텐데, 방법은 모르겠음
    """
    # get input data
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # do parametric search
    if N > M:
        time = 0
        l, r = 0, N*max(arr)
        while l <= r:
            cnt = M  # 굳이 안 내리고, 타기만 해도 되는거라, M으로 초기화
            mid = (l+r) // 2  # current time upper bound
            for nt in arr:
                cnt += mid // nt
                if cnt >= N:
                    break

            if cnt >= N:
                time = mid
                r = mid - 1
            else:
                l = mid + 1

        prev = M
        for nt in arr:
            prev += (time-1) // nt

        for i, nt in enumerate(arr):
            if not (time % nt):
                prev += 1

            if prev == N:
                print(i+1)
                break
    else:
        print(N)

if __name__ == "__main__":
    solution()
