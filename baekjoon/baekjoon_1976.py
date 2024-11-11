import sys
from collections import deque, defaultdict


def solution():
    """ 주어진 경로 validation
    condition 1: 중간에 다른 도시 경유 가능
        - E C => E-C, E-A-C, ... 모두 올바른 경로로 간주
        - 같은 도시 여러번 방문 가능

    constraint:
        - 스택 종료 혹은 루프 종료 조건을 뭘로 설정..?
            - 구간마다 visited를 바꿔주면 될거 같은데??
            - 같은 구간에서는 중복 경로 X, "더 이상 갈 곳 없으면 바로 끝"
            - 여행 경로 상 앞쪽에 있는거 나오면 못감
    idea: bfs
        - 인자: 출발-중간 목표 지점
        - 방문 선후 관계 고려하려면 dfs가 편할 것 같음
        - 스택 종료 조건: 더 이상 방문할 곳 없거나, 주어진 경로 방문 완료
        - 스택 호출 조건: 다음 방문할 곳 있을 떄
        - 방문 기록 조건:
            - 같은 서브 구간 내에서는 중복 허용 불가,
            - 방문 기록 배열은 중간 목적지 도달할 때마다, 초기화
    feedback:
        - 이런건 느낌이 딱 유니온 파인드잖아
            - 유니온 파인드가 맞는게, 경로가 있네 마네 탐색할 필요 없고, 주어진 경로가 그냥 같은 그래프 집합에 속하면 YES

    """
    # bfs function
    def bfs(x: int, y: int, cache: set) -> int:
        """
        Args:
            y: sub goal
            x: starting point
            cache: hash of do not visited in this stack
        """
        q = deque([x])
        visited.add(x)
        while q:
            vx = q.popleft()
            for nx in graph[vx]:
                if nx == y:
                    return 1

                if nx not in visited and nx not in cache:
                    q.append(nx)
                    visited.add(nx)

        return 0  # if cannot anyway

    # initialize the data structure
    input = sys.stdin.readline
    N = int(input())  # cities
    M = int(input())  # nums of planning
    graph = defaultdict(list)
    for i in range(N):
        col = list(map(int, input().split()))
        for j in range(N):
            if col[j]:
                graph[i+1].append(j+1)

    path = list(map(int, input().split()))
    for i in range(M-1):
        src, end = path[i], path[i+1]
        cannot = set(path[i+2:])
        visited = set()

        if bfs(src, end, cannot):
            continue
        else:
            print("NO")
            break
    else:
        print("YES")


def solution2():
    """
    경로가 존재한다: 같은 분리 집합에 존재한다
    => 따라서 직접 탐색하면서, 경로를 기록할 필요가 없고 같은 집합에 속하는지 여부만 판정해주면 된다

    idea: union-find
    feedback:
        - bfs는 왜 안될까...?
    """
    # union-find
    sys.setrecursionlimit(10**6)
    def find(x: int):
        if arr[x] != x:
            arr[x] = find(arr[x])
        return arr[x]

    def union(x: int, y: int) -> None:
        x = find(x)
        y = find(y)
        if x < y:
            arr[y] = x
        else:
            arr[x] = y

    input = sys.stdin.readline
    N = int(input())  # cities
    M = int(input())  # nums of planning
    arr = [i for i in range(0, N+1)]

    for i in range(N):
        col = list(map(int, input().split()))
        for j in range(N):
            if col[j] and find(i+1) != find(j+1):
                union(i+1, j+1)

    path = list(map(int, input().split()))
    src = arr[path[0]]
    answer = "YES"
    for i in range(1, M):
        cnt = arr[path[i]]
        if src != cnt:
            answer = "NO"
            break

    print(answer)

    return


if __name__ == "__main__":
    solution2()
