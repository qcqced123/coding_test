import sys
from collections import deque


def solution():
    """
    idea: dfs with indegree
        - 위상값 카운트
        - 시작 노드: 위상값 0
        - 위상별 dfs 수행
            - 하위 노드 개수 세어서 비교
    question:
        - N**2인데 왜 시간 초과가 날까
    """
    # dfs
    def dfs(x: int):
        nums = 0
        for nx in graph[x]:
            if not indegree[nx]:
                nums += dfs(nx)
            else:
                nums += indegree[nx]
                break

        if not nums: nums += 1
        indegree[x] = nums
        return nums

    # init the data structure
    sys.setrecursionlimit(10**6)
    input = sys.stdin.readline
    N, M = map(int, input().split())
    indegree = [0]*(N+1)
    graph = {k: [] for k in range(1, N+1)}

    for _ in range(M):
        child, parent = map(int, input().split())
        graph[parent].append(child)
        indegree[child] += 1

    # find the starting point of dfs
    src_point = []
    for i in range(1, N+1):
        if not indegree[i]: src_point.append(i)
        else: indegree[i] = 0

    # let's dfs
    answer = []
    count = 0
    for src in src_point:
        cnt = dfs(src)
        if cnt > count:
            answer = [src]
            count = cnt

        elif cnt == count:
            answer.append(src)

    print(*answer)


def solution2():
    # bfs
    def bfs(x: int):
        nums = 0
        q = deque([x])
        while q:
            vx = q.popleft()
            for nx in graph[vx]:
                if not indegree[nx]:
                    nums += 1

        return

    input = sys.stdin.readline
    N, M = map(int, input().split())
    indegree = [0] * (N + 1)
    graph = {k: [] for k in range(1, N + 1)}

    for _ in range(M):
        child, parent = map(int, input().split())
        graph[parent].append(child)
        indegree[child] += 1

    # find the starting point of dfs
    src_point = []
    for i in range(1, N + 1):
        if not indegree[i]:
            src_point.append(i)
        else:
            indegree[i] = 0

    # let's dfs
    answer = []
    count = 0
    for src in src_point:
        cnt = bfs(src)
        if cnt > count:
            answer = [src]
            count = cnt

        elif cnt == count:
            answer.append(src)

    print(*answer)

    return


if __name__ == "__main__":
    solution2()
