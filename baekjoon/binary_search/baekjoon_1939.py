import sys
from collections import deque, defaultdict


def solution():
    """ NlogN, 중량의 최대값, 이동: 공장1 to 공장2 (방향 제한은 없고)
    결국 이동 경로상에 존재하는 다리들의 조합 중에서, 중량 제한의 최소값이 중요함

    idea: binary search with hash
        - 가능한 경로 경우의 수부터 만들어야 할 것 같은데...?
        - 탐색 대상/범위: 중량 배열
        - 탐색 기준: 현재 "중량값"이 최대값이 되려면..? 만약 경로 중에 현재 기준값보다 큰게 나오면..?
        - 경로에

    question:
        - 경로를 효율적으로 만들어 줘야 하는데, 그걸 못하겠음
        - 경로는 BFS로
        - 아니 BFS 할거면, 굳이 이분 탐색으로 최대 중량값을 지정할 필요가 있어..?
        - 그래 그냥 풀어보자 일단
    """
    def bfs(x: int, y: int) -> int:
        result = 0
        q = deque([(x, sys.maxsize)])  # 노드 번호, 중량
        visited = set()
        while q:
            vx, vl = q.popleft()
            for nx, nl in graph[vx]:
                if nx == y:
                    result = max(result, nl)

                # visited 배열에 경로값도 넣어야 될듯
                # 이렇게 해야 정확한데, 메모리가 터지는구나, 그래서 이분탐색으로 최대한 종류를 줄여야!
                # 지금은 무향 그래프로 양쪽다 만들어서 visited 배열이 커지는 문제가 있는데, 이걸 유향으로 바꿔보자
                # 그럼 절반으로 줄어들지 않을까
                if nl > vl: nl = vl
                if (vx, nx, nl) not in visited and (nx, vx, nl) not in visited:
                    visited.add((vx, nx, nl)), visited.add((nx, vx, nl))
                    q.append((nx, nl))

        return result

    input = sys.stdin.readline
    N, M = map(int, input().split())  # 섬, 다리

    # init pointer and make graph
    # change no direction graph to directional graph
    graph = defaultdict(list)
    for _ in range(M):
        s, e, limit = map(int, input() .split())
        graph[s].append((e, limit)), graph[e].append((s, limit))

    # get starting point
    src, end = map(int, input().split())
    print(bfs(src, end))


def solution_bfs():
    """ baekjoon 1939
    idea: binary search with bfs, dfs
    """
    from collections import deque, defaultdict
    def bfs(x:int, y: int, weight: int) -> int:
        q = deque([(x, INF)])
        visited = [0]*(N+1)
        visited[x] = 1

        while q:
            vx, vl = q.popleft()
            for nx, nl in graph[vx]:
                if not visited[nx] and nl >= weight:
                    visited[nx] = 1
                    q.append((nx, nl))

        if visited[y]: return 1
        else: return 0

    # get the input and make the data structure
    INF = sys.maxsize
    input = sys.stdin.readline
    N, M = map(int, input().split())  # 노드, 엣지
    graph = defaultdict(list)

    l, r = 0, 0
    for _ in range(M):
        s, e, limit = map(int, input().split())
        graph[s].append((e, limit)), graph[e].append((s, limit))
        r = max(r, limit)

    answer = 0
    src, end = map(int, input().split())
    while l <= r:
        mid = (l+r) // 2
        if bfs(src, end, mid):
            answer = mid
            l = mid + 1

        else:
            r = mid - 1

    print(answer)


def solution_dfs():
    """ baekjoon 1939 with dfs & binary search
    """
    from collections import defaultdict
    # dfs function
    sys.setrecursionlimit(10**6)
    def dfs(x: int):
        """ 스택 종료 조건: 도착지점 도착 그리고 제약 사항 통과
        """
        if x == end:
            return 1

        for nx, nl in graph[x]:
            if not visited[nx] and nl >= mid:
                visited[nx] = 1
                cnt = dfs(nx)
                if cnt:
                    return 1
        return 0

    # get the input and make the data structure
    INF = sys.maxsize
    input = sys.stdin.readline
    N, M = map(int, input().split())  # 노드, 엣지
    graph = defaultdict(list)

    l, r = 0, 0
    for _ in range(M):
        s, e, limit = map(int, input().split())
        graph[s].append((e, limit)), graph[e].append((s, limit))
        r = max(r, limit)

    answer = 0
    src, end = map(int, input().split())
    while l <= r:
        mid = (l+r) // 2
        visited = [0]*(N+1)
        if dfs(src):
            answer = mid
            l = mid + 1

        else:
            r = mid - 1

    print(answer)


if __name__ == "__main__":
    solution_bfs()
    solution_dfs()
