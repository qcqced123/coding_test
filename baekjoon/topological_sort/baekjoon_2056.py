import sys
from collections import deque, defaultdict


def solution():
    """ N**2, 선행 순서(위상 정렬, dp), 번호가 선행 순서, 최소 시간
    선행 관계 없으면, 병렬 처리 가능
    input:
        입력 순서: 번호
        1번 원소: 시간
        2번 원소: 선행 작업 개수
        3번 원소 ~ : 선행 작업 번호

    idea: dynamic programming
        - graph with hash
        - 2D Table
            - row: 작업
            - col: 작업
            - update 기준:
    question:
        - 메모리가 터지는데, 381MB 필요함
        - 1D 배열로 풀어야 되나...? 어케 푸냐
    """
    # init data structure
    input = sys.stdin.readline
    N = int(input())
    arr = [0]*(N+1)
    graph = defaultdict(set)  # for connecting information of each task
    cache = [[0]*(N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        info = list(map(int, input().split()))
        arr[i] = info[0]
        if info[1]:
            for j in range(info[1]):
                graph[i].add(info[j+2])

    # get the last task
    last_task, cnt = 0, 0
    for k,v in graph.items():
        if len(v) > cnt:
            cnt = len(v)
            last_task = k

    # do the dynamic programming
    cache[1][1] = arr[1]
    for i in range(2, N+1):
        for j in range(1, N+1):
            # check the node info
            if j in graph[i]:
                cache[i][j] = max(cache[j][j], cache[i][j-1])

            elif i == j:
                cache[i][j] = cache[i][j-1] + arr[i]

            else:
                cache[i][j] = cache[i][j-1]

    print(cache[last_task][last_task])


def solution2() -> None:
    """ idea: topological sort with dynanmic programming
        - there are multiple starting point, so need to use cache array
    """
    # init data structure
    input = sys.stdin.readline
    N = int(input())
    arr = [0]*(N+1)  # array of time
    graph = {k: [] for k in range(1, N+1)}  # for connecting information of each task
    indegree = [0]*(N+1)
    for i in range(1, N+1):
        info = list(map(int, input().split()))
        arr[i] = info[0]
        if info[1]:
            indegree[i] = info[1]
            for j in range(info[1]):
                graph[info[j+2]].append(i)

    # find the starting point of graph
    src_point = []
    cache = [0] * (N+1)
    for i, n in enumerate(indegree):
        if i and not n:
            src_point.append(i)
            cache[i] = arr[i]

    q = deque(src_point)
    while q:
        vx = q.popleft()
        for nx in graph[vx]:
            indegree[nx] -= 1
            cache[nx] = max(cache[nx], cache[vx] + arr[nx])
            if not indegree[nx]:
                q.append(nx)
    print(max(cache))


if __name__ == "__main__":
    solution2()
