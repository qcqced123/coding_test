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


def solution2():
    """
    feedback:
        - 시간 복잡도 제한상, bfs만으로도 풀 수 있는게 맞음
        - 그런데, 공간 복잡도가 128mb, 문제 조건에 맞게 모든 경우의 수를 고려 하려면 최대 4byte*1만*10만 짜리 배열이 필요
        - 따라서, 공간 복잡도 제약을 가볍게 뛰어넘기 때문에, 이분 탐색이 필요함
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
                # 될리가 없네, 953메가...
                if nl > vl: nl = vl
                if (vx, nx, nl) not in visited:
                    visited.add((vx, nx, nl))
                    q.append((nx, nl))

        return result

    input = sys.stdin.readline
    N, M = map(int, input().split())  # 섬, 다리

    # init pointer and make graph
    # get starting point
    graph = defaultdict(list)
    tmp = [list(map(int, input().split())) for _ in range(M)]
    src, end = map(int, input().split())
    if src > end:
        src, end = end, src

    # change no direction graph to directional graph
    for s, e, l in tmp:
        if s > e and s != src: # 지금 이거 때메 그렇구나
            s, e = e, s
        graph[s].append((e,l))

    print(bfs(src, end))


def solution3():
    def bfs(x: int, y: int, limit: int) -> int:
        q = deque([(x, sys.maxsize)])  # 노드 번호, 중량
        visited = set()
        while q:
            vx, vl = q.popleft()
            for nx, nl in graph[vx]:
                if nx == y and nl >= limit:
                    return 1

                if nl > vl:
                    nl = vl

                if (vx, nx) not in visited:
                    visited.add((vx, nx))
                    q.append((nx, nl))

        return 0

    input = sys.stdin.readline
    N, M = map(int, input().split())  # 섬, 다리

    # init pointer and make graph
    # get starting point
    graph = defaultdict(list)
    tmp = [list(map(int, input().split())) for _ in range(M)]
    src, end = map(int, input().split())
    if src > end:
        src, end = end, src

    # change no direction graph to directional graph
    l, r = 0, -sys.maxsize
    for s, e, limit in tmp:
        r = max(r, limit)
        if s > e and s != src: # 지금 이거 때메 그렇구나
            s, e = e, s
        graph[s].append((e, limit))

    # binary search for reducing the memory complexity
    answer = 0
    while l <= r:
        mid = (l+r) // 2
        if bfs(src, end, mid):
            answer = mid
            l = mid + 1

        else:
            r = mid - 1

    print(answer)


def solution4():
    """
    그래프:
        - 무향 설계
        - 같은 구간 사이에 여러 다리가 있으면, 제한 높은거만 남기기
    bfs:
        - mid 값 이상 찾으면 바로 종료
        - visited가 제일 문제임
        - 직관적으로 dfs가 더 유리해보임
    """

    input = sys.stdin.readline
    N, M = map(int, input().split())  # 섬, 다리

    # init pointer and make graph
    # change no direction graph to directional graph
    graph = defaultdict(list)
    for _ in range(M):
        s, e, limit = map(int, input().split())
        graph[s].append((e, limit)), graph[e].append((s, limit))

    # get starting point
    src, end = map(int, input().split())


    return


def solution5():
    """
    그래프:
        - 무향 설계
        - 같은 구간 사이에 여러 다리가 있으면, 제한 높은거만 남기기
    dfs:
        - mid 값 이상 찾으면 바로 종료
        - visited가 제일 문제임
        - 직관적으로 dfs가 더 유리해보임
    """
    sys.setrecursionlimit(10**6)
    def dfs(x: int, y: int, curr: int, limit: int) -> int:
        for nx, nl in graph[x]:
            cnt = min(curr, nl)
            if nx == y:
                if cnt >= limit: return 1
                else: continue

            else:
                if nx not in visited:
                    visited.add(nx)
                    dfs(nx, y, cnt, limit)
        return 0

    INF = sys.maxsize
    input = sys.stdin.readline
    N, M = map(int, input().split())  # 섬, 다리

    # init pointer and make graph
    # change no direction graph to directional graph
    l, r = 0, -INF
    graph = defaultdict(list)
    for _ in range(M):
        s, e, limit = map(int, input().split())
        graph[s].append((e, limit)), graph[e].append((s, limit))
        r = max(r, limit)

    # get starting point
    src, end = map(int, input().split())

    # binary search for reducing the memory complexity
    answer = 0
    while l <= r:
        visited = set()
        mid = (l + r) // 2
        if dfs(src, end, INF, mid):
            answer = mid
            l = mid + 1

        else:
            r = mid - 1

    print(answer)

    return


def solution6():
    def bfs(x: int, y: int, limit: int) -> int:
        q = deque([x])
        visited = [0]*(N+1)
        visited[x] = 1
        while q:
            vx = q.popleft()
            for nx, nl in graph[vx]:
                if not visited[nx] and nl >= limit:
                    visited[nx] = True
                    q.append(nx)

        if visited[y]:
            return 1
        else:
            return 0

    INF = sys.maxsize
    input = sys.stdin.readline
    N, M = map(int, input().split())  # 섬, 다리

    # init pointer and make graph
    # change no direction graph to directional graph
    l, r = 0, -INF
    graph = defaultdict(list)
    for _ in range(M):
        s, e, limit = map(int, input().split())
        graph[s].append((e, limit)), graph[e].append((s, limit))
        r = max(r, limit)

    # get starting point
    src, end = map(int, input().split())

    # binary search for reducing the memory complexity
    answer = 0
    while l <= r:
        mid = (l+r) // 2
        if bfs(src, end, mid):
            answer = mid
            l = mid + 1
        else:
            r = mid - 1

    print(answer)



if __name__ == "__main__":
    solution6()
