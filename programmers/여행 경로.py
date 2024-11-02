import sys
from collections import defaultdict


def solution(tickets):
    """ 여행경로, N**2, 사전순 리턴, 모든 항공권 사용 필수
    idea 2: dfs with hash
        - 인자 정의: 현재 노드, 이전 경로, 이전 방문 캐시
    """
    # set up the module
    answer = []
    size = len(tickets)
    graph = defaultdict(list)
    visited = defaultdict(int)

    # init the graph and visited hash
    for ticket in tickets:
        src, end = ticket
        graph[src].append(end)
        visited[(src, end)] += 1

    # do the dfs search
    sys.setrecursionlimit(10 ** 6)

    def dfs(x, path, cache):
        if len(path) == size + 1:
            answer.append(path)
            return

        for nx in graph[x]:  # find next node
            if cache[(x, nx)]:  # current node's ticket is available
                cache[(x, nx)] -= 1
                dfs(nx, path + [nx], cache)
                cache[(x, nx)] += 1  # backtracking for other path

    dfs(
        "ICN",
        ["ICN"],
        visited
    )
    answer.sort()
    return answer[0]


if __name__ == "__main__":
    result = solution([
        ["EZE", "TIA"],
        ["EZE", "HBA"],
        ["AXA", "TIA"],
        ["ICN", "AXA"],
        ["ANU", "ICN"],
        ["ADL", "ANU"],
        ["TIA", "AUA"],
        ["ANU", "AUA"],
        ["ADL", "EZE"],
        ["ADL", "EZE"],
        ["EZE", "ADL"],
        ["AXA", "EZE"],
        ["AUA", "AXA"],
        ["ICN", "AXA"],
        ["AXA", "AUA"],
        ["AUA", "ADL"],
        ["ANU", "EZE"],
        ["TIA", "ADL"],
        ["EZE", "ANU"],
        ["AUA", "ANU"]
    ])
    print(result)
