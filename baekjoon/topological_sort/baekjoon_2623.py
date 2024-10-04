import sys
from collections import deque


def solution():
    """ 전체 가수의 순서를 정하기, 100,000,000, N^2*M
    idea: BFS with topological sorting
        1) 자신의 하위 모든 노드 전부 그래프에 삽입
3 3
3 1 2 3
2 3 2
2 1 3


4 2
2 4 2
3 4 2 1
    => 중복되는거 처리를 제대로 못함
    => 캐시 배열에 차수가 0이 아닌 애들은 출력이 안됨
    Reference:
        https://www.acmicpc.net/board/view/124998

    """
    N, M = map(int, sys.stdin.readline().split())  # singer, PD

    # initialize cache for topological sort, the graph
    cache = [0]*(N+1)
    graph = {i: [] for i in range(1, N+1)}
    arr_list = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
    for curr in arr_list:
        nums, *arr = curr
        for i in range(0, nums-1):
            j = i+1
            graph[arr[i]].append(arr[j])
            cache[arr[j]] += 1

    # initialize the queue with zero-grade
    q = deque([])
    for i in range(1, len(cache)):
        if not cache[i]:
            q.append(i)

    # do graph search
    result = []
    while q:
        vx = q.popleft()
        result.append(vx)
        for nx in graph[vx]:
            cache[nx] -= 1
            if not cache[nx]:
                q.append(nx)

    # 출력 배열 길이 != 전체 노드 개수: 순서 정하기 불가
    if len(result) != N:
        print(0)
    else:
        for i in result:
            print(i)


if __name__ == "__main__":
    solution()
