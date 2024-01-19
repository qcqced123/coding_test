import sys
from collections import defaultdict


def front_rotate(x: str):
    """ pure DFS
    """
    visit[char_map[x]] = True
    result_list.append(x)

    for node in tree[x]:
        if node != '.' and not visit[char_map[node]]:
            front_rotate(node)


def median_rotate(x: str):
    visit[char_map[x]], flag = True, True
    for idx, node in enumerate(tree[x]):
        if node != '.' and not visit[char_map[node]]:
            if idx == 1:
                flag = False
                result_list.append(x)
            median_rotate(node)
    if flag:
        result_list.append(x)


def back_rotate(x: str):
    visit[char_map[x]] = True
    for node in tree[x]:
        if node != '.' and not visit[char_map[node]]:
            back_rotate(node)
    result_list.append(x)


sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
tree, char_map = defaultdict(list), {}

for i in range(n):
    k, *v = list(map(str, sys.stdin.readline().split()))
    tree[k] = v
    char_map[k] = i


for func in [front_rotate, median_rotate, back_rotate]:
    result_list, visit = [], [False] * n
    func('A')
    print(''.join(result_list), end='\n')

