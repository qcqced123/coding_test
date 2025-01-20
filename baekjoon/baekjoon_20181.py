import sys
from collections import defaultdict

def solution():
    """ 이동 방향: left to right, 초당 1칸씩 오른쪽으로, 1칸 가는데 1초 소모, NlogN
    idea: prefix sum with parametric search, hash
        - 먹기 시작하면 쭉 먹어야 함 (연속된 부분 배열의 합, 1차원 배열의 누적합)
        - 멈추기 조건:
            - 합이 제약 조건 K 이상 or 더 이상 먹이가 없을 때 (이미 가장 오른쪽에 도달했을 때)
        - 탈피 에너지: 초과량 - K
        - 최대 탈피 에너지 구하기
        - 아 그니까 K를 넘길 때 확 크게 넘길수록 유리하네
        - 최적화 대상/범위: 최대 탈피 에너지, 1 to 10**8
    """
    # get input data
    input = sys.stdin.readline
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    # do parametric search
    answer = 0
    l, r = 1, int(1e+8)
    while l <= r:
        mid = (l+r) // 2
        cache = defaultdict(int)
        cnt, cache[0] = 0, 1
        for element in arr:
            cnt += element
            if cache[cnt-mid]:
                break

            cache[cnt] += 1

        else:
            r = mid - 1
            continue

        answer = mid
        l = mid + 1

    print(answer)

if __name__ == "__main__":
    solution()
