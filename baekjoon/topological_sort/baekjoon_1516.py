import sys
from collections import deque, defaultdict


def solution():
    """ 종족 벨런싱, 플레이 시간, 위상 정렬의 느낌이 스멀 스멀
    idea: topological sort with dynamic programming
        -
    """
    # init te data structure
    input = sys.stdin.readline
    N = int(input())  # number of nodes

    graph = defaultdict(list)
    src_point, indegree, cache = [], [0]*(N+1), [0]*(N+1)
    for i in range(1, N+1):  # number of current node
        temp = list(map(int, input().split()))
        if temp[1] == -1: temp[1] = 0
        time, preq = temp[:2]
        if not preq:
            cache[i] = time
            src_point.append(i)  # num of node, time
        else:
            graph[preq].append((i, time))  # time, num of node
            indegree[i] += 1

    # do topological sorting
    q = deque(src_point)
    while q:
        vx = q.popleft()
        vc = cache[vx]
        for nx, nc in graph[vx]:
            indegree[nx] -= 1
            cache[nx] = max(cache[nx], vc + nc)
            if not indegree[nx]:
                q.append(nx)

    for i in range(1, N+1):
        print(cache[i])


def solution2():
    # init te data structure
    INF = sys.maxsize
    input = sys.stdin.readline
    N = int(input())  # number of nodes

    graph = defaultdict(list)
    src_point, indegree, cache = [], [0]*(N+1), [0]*(N+1)
    for i in range(1, N+1):  # number of current node
        temp = list(map(int, input().split()))
        time, *cnt = temp
        if len(cnt) == 1:
            cache[i] = time
            src_point.append(i)  # num of node, time
            continue

        for j in cnt[:-1]:
            graph[j].append((i, time))  # time, num of node
            indegree[i] += 1

    # do topological sorting
    q = deque(src_point)
    while q:
        vx = q.popleft()
        vc = cache[vx]
        for nx, nc in graph[vx]:
            indegree[nx] -= 1
            cache[nx] = max(cache[nx], vc + nc)
            if not indegree[nx]:
                q.append(nx)

    for i in range(1, N + 1):
        print(cache[i])


if __name__ == "__main__":
    solution2()
