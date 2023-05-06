import sys
"""
이렇게 풀면 시간 초과...
"""


def dfs(start, total):
    global tmp_result
    if len(node_list[start]) == 0:
        tmp_result.append(total)
        return
    for node, weight in node_list[start]:
        dfs(node, total+weight)


sys.setrecursionlimit(10**9)
N = int(sys.stdin.readline())
node_list, final_result = [[] for _ in range(N+1)], []

for _ in range(N-1):
    src, end, cost = map(int, sys.stdin.readline().split())
    node_list[src].append([end, cost])

for i in range(1, N+1):
    result = []
    if len(node_list[i]) >= 1:
        for idx in node_list[i]:
            tmp_result = []
            dfs(idx[0], idx[1])
            result.append(max(tmp_result))
        result.sort(reverse=True)
        final_result.append(sum(result[0:2]))
print(max(final_result))


