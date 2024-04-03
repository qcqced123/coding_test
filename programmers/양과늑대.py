from collections import defaultdict, deque


def solution(info, edges):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/92343

    summary:
        1) 이진트리 그래프: 노드 종류는 늑대 or 양
          - 양 <= 늑대: 모든 양 사라짐
        => 양 안사라지게 하면서, 최대한 많은 양 수집해 루트로 복귀

    solution:
        1) BFS 탐색
          - visit 배열에 있어도 지나는 갈 수 있도록
    """

    def build_tree():
        tree = defaultdict(list)
        for edge in edges:
            src, end = edge
            tree[src].append(end)
        return tree

    answer = 0
    tree = build_tree()
    queue = deque([(0, 1, 0, set())])  # current node, nums of sheep, nums of wolfs, visit array
    while queue:
        print(queue)
        vy, vs, vw, visited = queue.popleft()
        answer = max(answer, vs)
        visited.update(tree[vy])  # add neighbor node into visit array, update() == add()
        for ny in visited:
            if info[ny]:
                if vs != vw + 1:
                    queue.append((ny, vs, vw + 1, visited - {ny}))
            else:
                queue.append((ny, vs + 1, vw, visited - {ny}))

    return answer

