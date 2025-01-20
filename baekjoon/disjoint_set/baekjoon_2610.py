import sys
from collections import defaultdict


def solution():
    """ 알고 있는 사람 == 같은 그룹, 그룹 개수 최대, 대표도 뽑고
    대표에게 의견 전달하려면, 아는 사람 통해서만, 최소 의사 전달 시간
    idea: union-find, floyd-warshall
        - group segmentation with union-find
        - find the optimal leader with floyd-warshall

    feedback:
        - union-find 로직상, 노드 사이의 연결 정보가 일정한 순서 없이, 무작위로 들어오면, 결과의 정확성 미보장
            - 그래서 모든 노드에 대해 find 한 번 더 수행 필요 (i != disjoint[i]인 경우, find() 다시 호출)
    """
    # disjoint set
    sys.setrecursionlimit(10**6)
    def find(x: int) -> int:
        if x != disjoint[x]:
            disjoint[x] = find(disjoint[x])
        return disjoint[x]

    def union(y: int, x: int) -> None:
        y = find(y)
        x = find(x)
        if y < x: disjoint[x] = y
        else: disjoint[y] = x

    # floyd-warshall
    def find_leader(g: list) -> int:
        # make data structure
        size = len(g)
        grid = [[INF]*size for _ in range(size)]
        for i in range(size):
            for j in range(size):
                if i != j and grid[i][j] == INF:
                    node1, node2 = g[i], g[j]
                    if node1 in graph[node2] and node2 in graph[node1]:
                        grid[i][j] = 1
                        grid[j][i] = 1

                elif i == j: grid[i][j] = 0

        for k in range(size):
            for i in range(size):
                for j in range(size):
                    if i != j:
                        grid[i][j] = min(grid[i][j], grid[i][k] + grid[k][j])

        answer, cache = INF, INF
        for i in range(size):
            cnt = max(grid[i])
            if cnt < cache:
                answer = g[i]
                cache = cnt

            elif cnt == cache:
                answer = min(answer, g[i])

        return answer

    # get input data
    INF = sys.maxsize
    input = sys.stdin.readline
    N = int(input())
    M = int(input())

    # init disjoint set, graph for finding leader
    graph = defaultdict(set)
    disjoint = [i for i in range(N+1)]
    for _ in range(M):
        src, end = map(int, input().split())
        graph[src].add(end), graph[end].add(src)
        if find(src) != find(end):
            union(src, end)

    # post-process for union-find
    for i in range(1, N+1):
        if i != disjoint[i]:
            disjoint[i] = find(i)

    # calculate the number of unique group
    # segment the each unique group
    K = 0
    group = defaultdict(list)
    for i in range(1, N+1):
        if i == disjoint[i]:
            K += 1
        group[disjoint[i]].append(i)

    print(K)

    # find the optimal leader with floyd-warshall
    answer = [find_leader(v) for k,v in group.items()]
    answer.sort()
    for a in answer:
        print(a)


if __name__ == "__main__":
    solution()
