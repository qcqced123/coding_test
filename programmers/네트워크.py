import sys


def my_solution(n, computers):
    """
    problem link:
        https://school.programmers.co.kr/learn/courses/30/lessons/43162

    summary:
        1) 같은 네트워크 상에 있다
          - 같은 그래프 안에 있다

    return:
        1) 상호 베타적인 그래프 혹은 집합이 몇 개 있음??

    solution:
        1) DFS 탐색
          - 인접 리스트 만들기
            - 키값과 같은 인덱스 넘어가기
            - 배열값 0 넘어가기
    => 제발 변수명 좀 알아보기 쉽게 쓰자
    => 정신 차리고 인자 넣자 제발
    """
    answer = 0
    visit = []
    graph = {i: j for i, j in enumerate(computers)}

    sys.setrecursionlimit(10 ** 6)

    def is_valid(curr_node, curr_state, node):
        return node != curr_node and curr_state and curr_node not in visit

    def dfs(x: int):
        for i, j in enumerate(graph[x]):
            curr_x, curr_s = i, j
            if is_valid(curr_x, curr_s, x):
                visit.append(curr_x)
                dfs(curr_x)

    for k in graph.keys():
        if k not in visit:
            visit.append(k);
            answer += 1
            dfs(k)
    return answer


def solution(n, computers):
    answer = 0
    return answer


