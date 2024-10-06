import sys
from collections import defaultdict


def solution():
    """ TSP: 시작 to 모든 노드 거쳐서 다시 복귀, 최소 비용, 중복 방문 불가
    입력 노드가 16개면...

    idea: back tracking
        1) 간선 정보 이용, 그래프 만들기

    => 시간 초과 ~
    => 한 번 백트래킹 할 떄, 모든 노드다 업데이트 해야할텐데, 모르겠다 어떻게하냐...;

    """
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 5)
    N = int(input())

    # initialize the grid, graph
    weights = []
    graph = defaultdict(list)
    for y in range(N):
        col = list(map(int, input().split()))
        for x in range(N):
            if col[x]:
                graph[y].append(x)

        weights.append(col)

    # backtrack function
    def backtrack(node: int, cost: int):
        """
        Args:
             node (int): number of current node
             cost (int): current cost of path
        """
        # end of search
        if len(visited) == N and node == src:
            answer[0] = min(answer[0], cost)
            return

        for nx in graph[node]:
            if nx not in visited:
                visited.add(nx)
                cnt = weights[node][nx]
                backtrack(nx, cost+cnt)  # 이러면 자연스럽게 back track이 된다.
                visited.remove(nx)  # for backtracking

    # update the answer
    # 한번 탐색할 떄 다 구해야
    answer = [sys.maxsize]
    for src in range(N):
        visited = set()
        backtrack(src, 0)

    print(answer[0])


def solution2():
    input = sys.stdin.readline
    N = int(input())

    weights = []
    return


if __name__ == "__main__":
    solution2()
