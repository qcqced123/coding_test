import sys
import copy
from itertools import combinations
from collections import deque, defaultdict


def solution2():
    """
    idea: backtracking with bfs
        - 선거구 분할: backtrack (combinations) 사용
        - 조합의 경우의 수가 실제 가능한 선거구인지 판정
            - bfs 이용
            - set도 mutable 이라서 함수의 인자로 넣을 때, 변경 된다는 점에 주의하자
    """
    # bfs func
    def bfs(curr: set, opponent: set) -> int:
        x = curr.pop()
        q = deque([x])
        opponent.add(x)
        result = populations[x]
        while q:
            vx = q.popleft()
            for nx in graph[vx]:
                if nx not in opponent and nx in curr:
                    q.append(nx)
                    curr.remove(nx)
                    opponent.add(nx)
                    result += populations[nx]

        return result if not curr else -1

    # init data structure
    INF = sys.maxsize
    input = sys.stdin.readline

    N = int(input())
    sectors = {i for i in range(1, N+1)}
    populations = [0] + list(map(int, input().split()))

    graph = defaultdict(list)
    for i in range(1, N+1):
        nums, *relations = list(map(int, input().split()))
        graph[i].extend(relations)

    # backtrack for each case
    # N//2+1: for optimization of combinations
    answer = INF
    for i in range(1, N//2+1):
        for comb in combinations(range(1, N+1), i):
            sector_a = set(comb)
            sector_b = sectors.difference(sector_a)
            population_a, population_b = bfs(sector_a, copy.deepcopy(sector_b)), bfs(sector_b, copy.deepcopy(sector_a))
            if population_a != -1 and population_b != -1:
                answer = min(answer, abs(population_a-population_b))

    print(answer) if answer != INF else print(-1)


if __name__ == "__main__":
    solution2()
