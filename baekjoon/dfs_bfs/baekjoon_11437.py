import sys


def solution():
    """
    idea: dfs with hash
        - 지금 코드는 그래프 만들 떄, 노드 번호가 작은쪽이 무조건 부모 노드라고 가정하고 풀었는데, 그게 아닌 경우도 있음
        - 1번 노드가 무조건 루트인건 맞지만, 그렇다고 번호가 작은쪽이 부모라고 설명하진 않았음...
        - 아래 반례가 그 증거
        - 그래프 구성하는 것부터 다시 짜야함
            - 그래프 구성하는 부분만 찾으면, 나머지는 그대로 사용해도 괜찮음
    feedback:
        - dfs 변형은 같은 논리로 잘 찾았는데, 최소 공통 조상을 찾는 방법이 따로 있...

    반례:
        4
        1 2
        3 4
        2 4
        1
        1 2
    """
    # dfs ops
    sys.setrecursionlimit(10**6)
    def dfs(x: int):
        path.append(x)
        visited[x] = 1
        for nx in graph[x]:
            if not visited[nx]:
                family[nx].extend(path)
                dfs(nx)

        path.pop()

    input = sys.stdin.readline
    N = int(input())

    # init graph structure
    graph = {i: [] for i in range(1, N+1)}
    family = {i: [i] for i in range(1, N+1)}
    for _ in range(N-1):
        src, end = map(int, input().split())
        graph[src].append(end)
        graph[end].append(src)

    # update the family structure
    path = []
    visited = [0]*(N+1)
    dfs(1)

    # answering the question
    # use set operation
    for _ in range(int(input())):
        src, end = map(int, input().split())
        print(max(set(family[src]) & set(family[end])))


def solution2():
    """
    idea: dfs with LCA
        - 무향 그래프 만들기
        - dfs 이용: 현재 노드의 깊이 구하기
        - 최소 공통 조상 찾기
            - 우선 깊이를 맞추기 (깊이가 맞아야 공통 조상을 찾으니까)
            - 깊이를 맞췄는데 아직도 양쪽 노드가 다르면, 계속 부모 노드를 찾기

    """
    # dfs func for calculating the depth of current node
    sys.setrecursionlimit(10**6)
    def dfs(x: int, depth: int) -> None:
        visited[x] = 1
        depths[x] = depth
        for nx in graph[x]:
            if not visited[nx]:
                parent[nx] = x
                dfs(nx, depth+1)

    # calculate the lca
    # 깊이에 맞춰서 하나씩 올리는구나!
    # 깊이가 같아져도, 둘이 다르면 다시 쭉...
    def lca(a: int, b: int) -> int:
        while depths[a] != depths[b]:
            if depths[a] > depths[b]:
                a = parent[a]
            else:
                b = parent[b]

        while a != b:
            a = parent[a]
            b = parent[b]

        return a

    input = sys.stdin.readline
    N = int(input())

    # init data structure
    parent = [0]*(N+1)
    depths = [0]*(N+1)
    visited = [0]*(N+1)
    graph = {i: [] for i in range(1, N+1)}
    for _ in range(N-1):
        src, end = map(int, input().split())
        graph[src].append(end)
        graph[end].append(src)

    dfs(1,0)

    for _ in range(int(input())):
        src, end = map(int, input().split())
        print(lca(src, end))

    return


if __name__ == "__main__":
    solution2()
