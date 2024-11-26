import sys
from collections import deque, defaultdict


def solution():
    """ 내리 사랑
    idea: topological sort with dynamic programming
        - 위상 배열 만들기, 인접 그래프 구조 만들기
        - 칭찬 배열 만들고, 직원 번호 오름차순으로 정렬
    point:
        - 설마 최종 보스가 여러명...?
        - 최종 보스도 칭찬 받을 수 있다...?
    """
    # init the data structure
    input = sys.stdin.readline
    N, M = map(int, input().split())  # num of nodes, num of edges
    relations = list(map(int, input().split()))  # for in-degree array
    praises = defaultdict(lambda: 0)
    for _ in range(M):
        k, v = map(int, input().split())
        praises[k] += v  # 더해야 함! 한 사람이 여러번 칭찬 받는게 가능하기 때문!

    # make the adj graph, in-degree arr, sort the praises arr
    src_point = []
    degree, cache = [0]*(N+1), [0]*(N+1)
    graph = defaultdict(list)
    for i in range(len(relations)):
        parent = relations[i]
        if parent == -1:
            src_point.append((i+1, praises[i+1]))
            cache[i+1] = praises[i+1]
            continue

        degree[i+1] += 1
        graph[parent].append((i+1, praises[i+1]))

    # do topological sort and update the dp cache
    q = deque(src_point)
    while q:
        vx, vp = q.popleft()
        for nx, np in graph[vx]:
            cache[nx] += vp + np
            degree[nx] -= 1
            if not degree[nx]:
                q.append((nx, cache[nx]))

    print(*cache[1:])


if __name__ == "__main__":
    solution()
