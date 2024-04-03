import heapq
from collections import defaultdict


def solution(n, costs):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/42861

    summary:
        1) 최소 비용으로 모든 섬이 통해 가능하도록
          - MST
          - 프림, 크루스칼 아무거나 가능
          - 양방향
    args:
        0, 1, 2 = src, end, cost

    solution:
        1) 정점 개수가 적으니까 프림을 써보자
    """

    def prim(src: int, visit) -> int:
        visit[src] = True
        candidate = grid[src]
        heapq.heapify(candidate)
        total = 0
        while candidate:
            vc, vs, ve = heapq.heappop(candidate)
            if not visit[ve]:
                total += vc
                visit[ve] = True

                for next_info in grid[ve]:
                    next_end = next_info[2]
                    if not visit[next_end]:
                        heapq.heappush(candidate, next_info)
        return total

    grid = defaultdict(list)
    for src, end, cost in costs:
        grid[src].append([cost, src, end]), grid[end].append([cost, end, src])

    visited = [False] * n
    answer = prim(0, visited)
    return answer

