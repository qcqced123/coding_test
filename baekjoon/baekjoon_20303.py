import sys


def solution():
    """ 분리 집합, 같은 집단의 모든 사탕 빼앗기, K명 이하에서 최대한 많은 사탕 빼앗기
    NlogM (N: 노드, M: 간선)

    idea: 무향 그래프, 분리 집합
        1) 분리 집합
        2) 집합별, 합계 사탕 숫자, 인원수 파악
        3) Knapsack 풀기
    """
    def find(x: int) -> int:
        if group[x] != x:
            group[x] = find(group[x])
        return group[x]

    def union(y: int, x: int) -> None:
        y = find(y)
        x = find(x)
        if y < x:
            group[x] = y
        else:
            group[y] = x

    N, M, K = map(int, sys.stdin.readline().split())
    arr = [0] + list(map(int, sys.stdin.readline().split()))  # 사탕 계산용
    group = list(range(N+1))  # 분리 집합

    for _ in range(M):
        src, end = map(int, sys.stdin.readline().split())
        if find(src) != find(end):
            union(src, end)

    candy_dict = {}
    member_dict = {}
    for i in range(1, N+1):
        root = group[i]
        if not root in candy_dict:
            candy_dict[root] = arr[i]
            member_dict[root] = 1
        else:
            candy_dict[root] += arr[i]
            member_dict[root] += 1

    info = [[n, c] for n, c in zip(member_dict.values(), candy_dict.values())]  # 인원수, 사탕
    info.sort()
    knapsack = [[0]*K for _ in range(len(info)+1)]
    for r in range(1, len(info)+1):  # index of group
        for c in range(1, K):  # weight
            cnt_nums, cnt_values = info[r-1]
            if cnt_nums <= c:  # 담을 수 있는 경우
                knapsack[r][c] = max(cnt_values + knapsack[r-1][c-cnt_nums], knapsack[r-1][c])
            else:
                knapsack[r][c] = knapsack[r-1][c]

    print(knapsack[-1][-1])


if __name__ == "__main__":
    solution()
