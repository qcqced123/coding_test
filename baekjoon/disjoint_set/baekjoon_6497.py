import sys
import heapq


def solution():
    """ not floyd-warshall, O(N+M)
    idea: prim
        - 우선순위 큐: 최소의 간선값 선택을 위해
        - 사이클 발생: 유니온 파인드
        - 현재 최소의 간선값이 사이클을 발생시키는지 확인
            - 사이클 X: MST 집합에 넣기
            - 사이클 0: 건너 뛰기
    """
    # check current two nodes are available
    sys.setrecursionlimit(10**5)
    def find(x: int):
        if parent[x] != x: parent[x] = find(parent[x])
        return parent[x]

    def union(y: int, x: int):
        y = find(y)
        x = find(x)
        if x > y: parent[y] = x
        else: parent[x] = y

    # prim func
    def prim() -> int:
        mst = []
        heapq.heapify(candidate)
        while candidate:
            vc, vs, ve = heapq.heappop(candidate)
            if find(vs) != find(ve):
                union(vs, ve)
                mst.append(vc)

        return sum(mst)

    def kruskal() -> int:
        mst = []
        candidate.sort()
        for i in range(len(candidate)):
            vc, vs, ve = candidate[i]
            if find(vs) != find(ve):
                union(vs, ve)
                mst.append(vc)

        return sum(mst)

    input = sys.stdin.readline
    while True:
        M, N = map(int, input().split())
        if not M and not N:
            return

        # init data structure
        total, candidate = 0, []
        for _ in range(N):
            src, end, cost = map(int, input().split())
            total += cost
            candidate.append((cost, src, end))

        # init disjoint set
        parent = [i for i in range(M)]
        print(total - kruskal())


if __name__ == "__main__":
    solution()
