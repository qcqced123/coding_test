import sys


def solution():
    """
    idea: dynamic programming
        - 제약 조건: 체력 (0이하가 되면 도로묵)
    feedback:
        - 제발 점화식 손으로 다 쓰고 풀자
        - 있는대로 머리로 어림 짐작 때려서 풀지말고 제바ㅏㄹ.....
    """
    # init data structure
    input = sys.stdin.readline
    N = int(input())
    cost = [0] + list(map(int, input().split()))
    happy = [0] + list(map(int, input().split()))
    cache = [[0]*100 for _ in range(N+1)]

    # do update the dp cache
    for i in range(1, N+1):
        cnt_cost = cost[i]
        cnt_happy = happy[i]
        if cnt_cost < 100:
            cache[i][cnt_cost] = max(cache[i - 1][cnt_cost], cache[i][cnt_cost], cnt_happy)

        for j in range(100):
            cache[i][j] = max(cache[i][j], cache[i-1][j])
            if cache[i-1][j] and j+cnt_cost < 100:
                cache[i][j+cnt_cost] = max(cache[i][j+cnt_cost], cache[i-1][j] + cnt_happy)

    print(max(cache[-1]))


if __name__ == "__main__":
    solution()
