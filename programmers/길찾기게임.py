from collections import defaultdict


def solution(nodeinfo):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/42892

    solution:
        1) (y축 기준 내림차순 정렬, x축 기준 오름차순 정렬)
        2) 좌표 테이블을 BST 배열로 전환
          - 이거 어떻게 해서든 구현한다 진짜
        3) 전위, 후위 순위 구현
    """
    nodeinfo_dict = {i + 1: j for i, j in enumerate(nodeinfo)}
    nodeinfo_dict = dict(sorted(nodeinfo_dict.items(), key=lambda x: (x[1][1], -x[1][0]), reverse=True))

    graph = {k: [None, None] for k in nodeinfo_dict.keys()}
    arr = list(nodeinfo_dict.items())

    answer = [[]]
    return answer


if __name__ == '__main__':
    print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))