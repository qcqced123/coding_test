import sys


def my_solution(nodeinfo):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/42892

    solution:
        1) (y축 기준 내림차순 정렬, x축 기준 오름차순 정렬)
        2) 좌표 테이블을 BST 배열로 전환
          - recursive call 이용해 Binary Tree 만들기
        3) 전위, 후위 순위 구현
    """
    def make_tree(src: int, root: int):
        left, right = graph[root][0], graph[root][1]
        if src < root:
            if left is None:
                graph[root][0] = src
                return

            else:
                make_tree(src, left)

        else:
            if right is None:
                graph[root][1] = src
                return

            else:
                make_tree(src, right)
        return

    def preorder(x: int, arr):
        if x is not None:
            arr.append(x2node[x])
            left, right = graph[x][0], graph[x][1]
            preorder(left, arr)
            preorder(right, arr)

    def postorder(x: int, arr):
        if x is not None:
            left, right = graph[x][0], graph[x][1]
            postorder(left, arr)
            postorder(right, arr)
            arr.append(x2node[x])

    sys.setrecursionlimit(10 ** 6)
    x2node = {j[0]: i + 1 for i, j in enumerate(nodeinfo)}
    nodeinfo_dict = {i + 1: j for i, j in enumerate(nodeinfo)}
    nodeinfo_dict = dict(sorted(nodeinfo_dict.items(), key=lambda x: (x[1][1], -x[1][0]), reverse=True))

    graph = {k: [None, None] for k, _ in nodeinfo_dict.values()}
    root_node = list(graph.keys())
    for k in root_node[1:]:
        make_tree(k, root_node[0])

    pre_arr, post_arr = [], []
    preorder(root_node[0], pre_arr), postorder(root_node[0], post_arr)
    answer = [pre_arr, post_arr]
    return answer


if __name__ == '__main__':
    print(my_solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))