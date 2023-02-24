import sys, heapq
"""
[Union Find 구현]
- Union: 노드를 합치는 연산
- Find: 현재 노드의 루트 노드를 찾는 연산
- 노드 번호는 0부터 시작 
"""
# Graph represented by Array
graph = [1, 1, 0, 0, 1, 5, 6]

def find(graph, x):
    """
    [parameter explain]
    - graph: tree which is represented by array
    - x: node number
    """
    if graph[x] != x:
        find(graph, graph[x])
    return x


