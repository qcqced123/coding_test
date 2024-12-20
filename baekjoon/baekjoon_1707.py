import sys
from collections import defaultdict


def solution():
    """ 게리 멘더링 문제를 역으로, 입력이 너무 커서 조합 사용한 귀납적 풀이는 불가
    idea: dfs
        - 연결 노드 개수가 가장 적은 위치 찾기:
            - 가장 작은 위치 중에서 하나 잡아서, dfs 수행
            - 인접한 노드는 다른 집합에, 인접 X는 같은 집합
            - 완성된 두 집합 정보 가지고, 인접 하는지 안하는지 판정

    question:
        - 몰라서 거의 찍다시피 풀었음

    reference:
        - https://www.acmicpc.net/board/view/145881
        - https://www.acmicpc.net/board/view/77198
    """
    INF = sys.maxsize
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)

    # grouping func
    def grouping(x: int, state: int) -> None:
        cache[x] = 1
        for nx in graph[x]:
            if not cache[nx]:
                if not state: group_b.add(nx)
                else: group_a.add(nx)
                grouping(nx, (state+1)%2)

    # check func
    def check(group: set) -> int:
        for x in group:
            for nx in graph[x]:
                if nx in group:
                    return 0
        return 1


    for _ in range(int(input())):
        # make the graph structure
        graph = defaultdict(list)
        V, E = map(int, input().split())
        cache = [0]*(V+1)
        for _ in range(E):
            src, end = map(int, input().split())
            cache[src] += 1
            cache[end] += 1
            graph[src].append(end), graph[end].append(src)

        # find the minimum connected node
        src_list, src_cache = [], INF
        for i in range(1, V+1):
            if cache[i] < src_cache:
                src_list = [i]
                src_cache = cache[i]
            elif cache[i] == src_cache:
                src_list.append(i)

        # re-init the cache structure for visited array
        for i in range(1, V+1):
            cache[i] = 0

        # do dfs
        # state 0: must add to group_b, state 1: must add to group_a
        for src in src_list:
            group_a = {src}
            group_b = set()
            grouping(src, 0)
            print(group_a, group_b)

            # check the current state of grouping
            flag_a, flag_b = check(group_a), check(group_b)
            if not flag_a or not flag_b:
                print("NO")
                break

        else: print("YES")


if __name__ == "__main__":
    solution()
