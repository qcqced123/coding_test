import sys
import heapq
from typing import List, Dict


def dijkstra(x: int, distance: List, graph: Dict[int, List]) -> Dict:
    h, distance[x], path = [], 0, {k: [] for k in graph.keys()}
    path[x].append(x), heapq.heappush(h, (distance[x], x))
    while h:
        vw, vx = heapq.heappop(h)
        if vw > distance[vx]:
            continue

        for i in graph[vx]:
            curr_cost, curr_node = i
            new_cost = vw + curr_cost
            if new_cost < distance[curr_node]:
                distance[curr_node], v_path = new_cost, path[vx]
                heapq.heappush(h, (new_cost, curr_node))
                path[curr_node] = v_path[:] + [curr_node]
            elif new_cost == distance[curr_node]:
                v_path = path[vx]
                path[curr_node] = v_path[:] + [curr_node]
    return path


def solution():
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())

    weights, grid = [float('inf')]*(n+1), {k: [] for k in range(1, n+1)}
    for _ in range(m):
        src, end, cost = map(int, sys.stdin.readline().split())
        grid[src].append((cost, end))

    src, end = map(int, sys.stdin.readline().split())
    result = dijkstra(src, weights, grid)

    print(weights[end])
    print(len(result[end]))
    print(*result[end])


if __name__ == "__main__":
    solution()
